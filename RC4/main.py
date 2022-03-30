#!/usr/bin/python
import sys

from const import DEFAULT_EN_KEYS, DEFAULT_UA_KEYS
from services.cipher import bruteforce, full_decrypt, full_encrypt
from utils.cli import get_arguments
from utils.file import read_docx, read_txt, write_docx, write_txt


def main():
    arguments = get_arguments()

    in_file, out_file = arguments.input_file, arguments.output_file
    locale = arguments.locale
    file_format = arguments.format

    default_keys = DEFAULT_UA_KEYS if locale == "UA" else DEFAULT_EN_KEYS

    in_text = read_docx(in_file) if file_format == "docx" else read_txt(in_file)
    keys = (arguments.key1, arguments.key2)

    if arguments.encrypt:
        keys = keys if all(keys) else default_keys

        result = full_encrypt(in_text, locale, *keys)
    else:
        if all(keys):
            result = full_decrypt(in_text, locale, *keys)
        else:
            result = bruteforce(msg=in_text, locale=locale)

    if file_format == "docx":
        write_docx(out_file, result)
    else:
        write_txt(out_file, result)

    return 0


if __name__ == "__main__":
    sys.exit(main())
