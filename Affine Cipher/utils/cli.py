import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Script to encrypt/decrypt data with Affine Cipher."
    )

    method_group = parser.add_mutually_exclusive_group(required=True)
    method_group.add_argument(
        "-e",
        "--encrypt",
        action="store_true",
        help="Encrypt message",
    )
    method_group.add_argument(
        "-d",
        "--decrypt",
        action="store_true",
        help="Decrypt message",
    )

    parser.add_argument(
        "-i",
        "--input-file",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-o",
        "--output-file",
        type=str,
        required=True,
    )

    parser.add_argument("-k", "--key", type=int, help="Key for the Affine cipher", required=False)

    return parser.parse_args()
