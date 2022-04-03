import argparse
import datetime
import os
import pickle
import socket
import threading

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from ellipticcurve import Ecdsa, PrivateKey
from termcolor import colored


class Server:
    def __init__(self, port: int) -> None:
        self.host = "127.0.0.1"
        self.port = port

    def start_server(self) -> None:
        """
        Generate the public and private keys to share.
        And a random secret key for AES.
        """
        self.generate_keys()
        secret_key = get_random_bytes(16)

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

        self._socket.bind((self.host, self.port))
        self._socket.listen(100)

        print(colored(f"[+] Running on host: {self.host}", "yellow"))
        print(colored(f"[+] Running on port: {self.port}", "yellow"))

        self.username_lookup = {}

        while True:
            sock, _ = self._socket.accept()
            username = sock.recv(1024).decode()

            print(colored(f"[+] New connection. Username: {username}", "yellow"))
            self.broadcast(
                colored(f" New person joined the room. Username: {username}", "yellow")
            )

            self.username_lookup[sock] = username
            self.clients.append(sock)

            # Exchange the public key with the client
            client_pub_key = self.send_public(sock)

            # Send signature
            self.send_signature(sock)

            # Encrypt the secret with the client public key
            encrypted_secret = self.encrypt_secret(client_pub_key, secret_key)

            self.send_secret(sock, encrypted_secret)
            threading.Thread(target=self.handle_client, args=(sock,)).start()

    def broadcast(self, msg: str) -> None:
        """
        Sending broadcast messages.
        """
        for _ in self.clients:
            print(colored(f"[+] Broadcast message: {msg}", "red"))

    @staticmethod
    def generate_keys() -> None:
        """
        Generate the public and private key pair.
        """
        try:
            private_key = RSA.generate(2048)
            public_key = private_key.publickey()

            private_key_pem = private_key.exportKey().decode()
            public_key_pem = public_key.exportKey().decode()

            sig_private_key = PrivateKey()
            sig_private_key_pem = sig_private_key.toPem()

            with open("server_private_key.pem", "w") as private:
                private.write(private_key_pem)

            with open("server_public_key.pem", "w") as public:
                public.write(public_key_pem)

            with open("server_sign_private_key.pem", "w") as private:
                private.write(sig_private_key_pem)

        except Exception as e:
            print(e)

    @staticmethod
    def encrypt_secret(client_pub_key: bytes, secret_key: bytes) -> bytes:
        """
        Encrypt the secret with the client public key.
        """
        try:
            cpKey = RSA.importKey(client_pub_key)
            cipher = PKCS1_OAEP.new(cpKey)
            encrypted_secret = cipher.encrypt(secret_key)

            return encrypted_secret

        except Exception as e:
            print(e)

    @staticmethod
    def send_secret(client: socket, secret_key: bytes) -> None:
        """
        Exchanging the secret key with the client.
        """
        try:
            client.send(secret_key)
            print(colored("[+] Secret key had been sent to the client", "yellow"))

        except Exception as e:
            print(e)

    @staticmethod
    def send_signature(client: socket) -> None:
        try:
            sign_public_key = PrivateKey.fromPem(
                open("server_sign_private_key.pem").read()
            ).publicKey()
            client.send(sign_public_key.toPem().encode("latin-1"))
            print(colored("[+] Signature had been sent to the client", "yellow"))

        except Exception as e:
            print(e)

    @staticmethod
    def send_public(client: socket) -> bytes:
        """
        Exchanging the public key with the client.
        """
        try:
            public_key = RSA.importKey(open("server_public_key.pem").read())
            client.send(public_key.exportKey())

            client_pub_key = client.recv(1024)
            print(colored("[+] Client public key had been received", "yellow"))

            return client_pub_key

        except Exception as e:
            print(e)

    def handle_client(self, client: socket) -> None:
        """
        Handle client.
        """
        sig_private_key = PrivateKey.fromPem(open("server_sign_private_key.pem").read())

        while True:
            try:
                msg = client.recv(1024)
            except:
                client.shutdown(socket.SHUT_RDWR)
                self.clients.remove(client)
                self.broadcast(f"{self.username_lookup[client]} has left.")
                break

            if msg.decode() != "":
                current_time = datetime.datetime.now()
                print(
                    colored(
                        f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} Message exchanged",
                        "blue",
                    )
                )
                for connection in self.clients:
                    if connection != client:
                        connection.send(msg)
                        connection.send(
                            pickle.dumps(Ecdsa.sign(msg.decode(), sig_private_key))
                        )
            else:
                print(
                    colored(
                        f"[+] {self.username_lookup[client]} left the server.", "red"
                    )
                )
                for conn in self.clients:
                    if conn == client:
                        self.clients.remove(client)
                break


def terminate(server: Server) -> None:
    while True:
        command = input("")
        if command == "TERMINATE":
            for conn in server.clients:
                conn.shutdown(socket.SHUT_RDWR)
            print(colored("[+] All connections had been terminated", "yellow"))
        break

    print(colored("[+] Server is shut down", "yellow"))
    os._exit(0)


if __name__ == "__main__":
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument(
        "-p", "--port", type=int, required=True, help="Port to run the server"
    )
    args = arg_parse.parse_args()

    main_server = Server(args.port)
    terminate = threading.Thread(target=terminate, args=(main_server,))

    terminate.start()
    main_server.start_server()
