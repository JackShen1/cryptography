import argparse
import sys


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Script to encrypt/decrypt data with RC4 Cipher."
    )

    method_group = parser.add_mutually_exclusive_group(required=True)
    method_group.add_argument(
        "-e", "--encrypt", action="store_true", help="Encrypt message"
    )
    method_group.add_argument(
        "-d", "--decrypt", action="store_true", help="Decrypt message"
    )

    parser.add_argument(
        "-f", "--format", type=str, choices=["docx", "txt"], required=True
    )

    parser.add_argument("-l", "--locale", type=str, choices=["UA", "EN"], required=True)

    parser.add_argument("-i", "--input-file", type=str, required=True)

    parser.add_argument("-o", "--output-file", type=str, required=True)

    parser.add_argument(
        "-k1", "--key1", type=str, help="Key1 for the RC4 cipher", required=False
    )
    parser.add_argument(
        "-k2",
        "--key2",
        type=str,
        help="Key2 for the RC4 cipher",
        required="--key1" in sys.argv,
    )

    return parser.parse_args()
