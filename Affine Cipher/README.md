**Affine Cipher**
==================

Annotation
----------

This script is designed to encrypt and decrypt text from a file and then save encrypted or decrypted text to a new file. Encryption algorithm - Affine cipher. The script itself can determine key, if it is not specified. The available arguments for the script are listed in the following paragraph.

Current options
---------------

| Short Form |   Long Form   |                Description                |
|:----------:|:-------------:|:-----------------------------------------:|
|     -e     |   --encrypt   |              Encrypt message              |
|     -d     |   --decrypt   |              Decrypt message              |
|     -i     |  --input-file |     File with text to encrypt/decrypt     |
|     -o     | --output-file | Output file with encrypted/decrypted text |
|     -k     |     --key     |          Key for the Affine cipher        |

**Note:** You can use either `--encrypt` or` --decrypt` argument, but not both at once, the program will not allow it, also one of the arguments must be present when calling the script. You can also use `--key`.

Usage
-----

Encrypt text with random key:
``` bash
$ python main.py -e -i "data/encrypt.docx" -o "data/decrypt.docx"
$ python main.py --encrypt --input-file "data/encrypt.docx" --output-file "data/decrypt.docx"
```

Encrypt text with own key:
``` bash
$ python main.py -e -i "data/encrypt.docx" -o "data/decrypt.docx" -k 5555
$ python main.py --encrypt --input-file "data/encrypt.docx" --output-file "data/decrypt.docx" --key 5555
```

Decrypt text:
``` bash
$ python main.py -d -i "data/decrypt.docx" -o "data/encrypt.docx"
$ python main.py --decrypt --input-file "data/decrypt.docx" --output-file "data/encrypt.docx"
```

Decrypt text with known key:
``` bash
$ python main.py -d -i "data/decrypt.docx" -o "data/encrypt.docx" -k 5555
$ python main.py --decrypt --input-file "data/decrypt.docx" --output-file "data/encrypt.docx" --key 5555
```
