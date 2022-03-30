**RC4 Cipher**
==================

Annotation
----------

This script is designed to encrypt and decrypt text from a file and then save encrypted or decrypted text to a new file. Encryption algorithm - RC4. The script itself can determine keys, if it is not specified. The available arguments for the script are listed in the following paragraph.

Current options
---------------

| Short Form |   Long Form   |                Description                |
|:----------:|:-------------:|:-----------------------------------------:|
|     -e     |   --encrypt   |              Encrypt message              |
|     -d     |   --decrypt   |              Decrypt message              |
|     -i     |  --input-file |     File with text to encrypt/decrypt     |
|     -o     | --output-file | Output file with encrypted/decrypted text |
|     -f     |   --format    |   Format of input/output file (txt/docx)  |
|     -l     |   --locale    |        Language of message (UA/EN)        |
|    -k1     |    --key1     |         Key1 for the Affine cipher        |
|    -k2     |    --key2     |         Key2 for the Affine cipher        |

**Note:** You can use either `--encrypt` or` --decrypt` argument, but not both at once, the program will not allow it, also one of the arguments must be present when calling the script. You can also use `--key1` with `--key2`.

Usage
-----

Encrypt text with default keys:
``` bash
$ python main.py -e -i "data/encrypt.txt" -o "data/decrypt.txt" -f "txt" -l "UA"
$ python main.py --encrypt --input-file "data/encrypt.docx" --output-file "data/decrypt.docx" -f "docx" -l "EN"
```

Encrypt text with own key:
``` bash
$ python main.py -e -i "data/encrypt.txt" -o "data/decrypt.txt" -f "txt" -l "UA" -k1 "Русні" -k2 "гайки"
$ python main.py --encrypt --input-file "data/encrypt.docx" --output-file "data/decrypt.docx" -f "docx" -l "EN" -k1 "text" -k2 "random"
```

Decrypt text:
``` bash
$ python main.py -d -i "data/decrypt.txt" -o "data/encrypt.txt" -f "txt" -l "UA"
$ python main.py --decrypt --input-file "data/decrypt.docx" --output-file "data/encrypt.docx" -f "docx" -l "EN"
```

Decrypt text with known key:
``` bash
$ python main.py -d -i "data/decrypt.txt" -o "data/encrypt.txt" -f "txt" -l "UA" -k1 "Русні" -k2 "гайки"
$ python main.py --decrypt --input-file "data/decrypt.docx" --output-file "data/encrypt.docx" -f "docx" -l "EN" -k1 "text" -k2 "random"
```
