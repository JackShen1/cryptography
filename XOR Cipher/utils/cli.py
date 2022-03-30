import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Script to encrypt/decrypt data with XOR Cipher."
    )

    method_group = parser.add_mutually_exclusive_group(required=True)
    method_group.add_argument(
        "-e", "--encrypt", action="store_true", help="Encrypt message"
    )
    method_group.add_argument(
        "-d", "--decrypt", action="store_true", help="Decrypt message"
    )

    parser.add_argument(
        "-i",
        "--input-file",
        type=argparse.FileType("r", encoding="UTF-8"),
        required=True,
    )

    parser.add_argument(
        "-o",
        "--output-file",
        type=argparse.FileType("w", encoding="UTF-8"),
        required=True,
    )

    key_group = parser.add_mutually_exclusive_group(required=False)
    key_group.add_argument("-k", "--key", type=str, help="Key for the XOR cipher")
    key_group.add_argument(
        "-m", "--max-key-len", type=int, help="Maximum length of the key"
    )
    key_group.add_argument("-l", "--key-len", type=int, help="Length of the key")

    return parser.parse_args()
