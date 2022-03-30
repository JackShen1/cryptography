#!/usr/bin/python
import sys

from services.cipher import decrypt, encrypt, find_key_len, find_xor_key
from utils.cli import get_arguments


def main():
    arguments = get_arguments()

    if arguments.encrypt:
        in_file, out_file = arguments.input_file, arguments.output_file

        plaintext = in_file.read()
        key = arguments.key if arguments.key else None
        out_file.write(encrypt(plaintext, key).decode())
    else:
        in_file, out_file = arguments.input_file, arguments.output_file

        ciphertext = bytearray(in_file.read().encode())

        key = arguments.key
        key_len = arguments.key_len
        max_key_len = arguments.max_key_len

        if key:
            key = bytearray(key.encode())
        elif key_len:
            key = find_xor_key(ciphertext, key_len)
        else:
            prob_lens = find_key_len(ciphertext=ciphertext, max_len=max_key_len)

            print("Probable key lengths: ")
            for prc, length in prob_lens:
                print(f"\t{length} - {prc}%")
            key_len = prob_lens[0][1]

            key = find_xor_key(ciphertext, key_len)

        out_file.write(decrypt(ciphertext=ciphertext, key=key).decode())

    in_file.close()
    out_file.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
