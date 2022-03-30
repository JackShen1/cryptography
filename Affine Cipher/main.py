#!/usr/bin/python
import sys

from services.cipher import decrypt, encrypt, find_affine_key, gen_random_key
from utils.cli import get_arguments
from utils.file import read_docx, write_docx


def main():
    arguments = get_arguments()

    if arguments.encrypt:
        in_file, out_file = arguments.input_file, arguments.output_file

        plaintext = read_docx(in_file)
        key = arguments.key if arguments.key else gen_random_key()
        write_docx(out_file, encrypt(encrypt(plaintext, key), key))
    else:
        in_file, out_file = arguments.input_file, arguments.output_file

        ciphertext = read_docx(in_file)

        key = arguments.key

        if key:
            decrypted = decrypt(decrypt(ciphertext, key), key)
            write_docx(out_file, decrypted)
        else:
            keys = find_affine_key(ciphertext)
            for key in keys:
                print(key)

    return 0


if __name__ == "__main__":
    sys.exit(main())
