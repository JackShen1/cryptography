**XOR Cipher**
==================

Annotation
----------

This script is designed to encrypt and decrypt text from a file and then save encrypted or decrypted text to a new file. Encryption algorithm - XOR cipher. The script itself can determine the most plausible length of the key and the key itself, if it is not specified. The available arguments for the script are listed in the following paragraph.

Current options
---------------

| Short Form |   Long Form   |                Description                |
|:----------:|:-------------:|:-----------------------------------------:|
|     -e     |   --encrypt   |              Encrypt message              |
|     -d     |   --decrypt   |              Decrypt message              |
|     -i     |  --input-file |     File with text to encrypt/decrypt     |
|     -o     | --output-file | Output file with encrypted/decrypted text |
|     -k     |     --key     |           Key for the XOR cipher          |
|     -m     | --max-key-len |         Maximum length of the key         |
|     -l     |   --key-len   |             Length of the key             |

**Note:** You can use either `--encrypt` or` --decrypt` argument, but not both at once, the program will not allow it, also one of the arguments must be present when calling the script. You can also use either `--key`, `--key-len` or `--max-key-len` or none of them.

Usage
-----

Encrypt text with random string:
``` bash
$ python main.py -e -i "data/plaintext.txt" -o "data/ciphertext.txt"
$ python main.py --encrypt --input-file "data/plaintext.txt" --output-file "data/ciphertext.txt"
```

Encrypt text with own key:
``` bash
$ python main.py -e -i "data/plaintext.txt" -o "data/ciphertext.txt" -k "spirit"
$ python main.py --encrypt --input-file "data/plaintext.txt" --output-file "data/ciphertext.txt" --key "spirit"
```

Decrypt text:
``` bash
$ python main.py -d -i "data/ciphertext.txt" -o "data/result.txt"
$ python main.py --decrypt --input-file "data/ciphertext.txt" --output-file "data/result.txt"
```

Decrypt text with known key:
``` bash
$ python main.py -d -i "data/ciphertext.txt" -o "data/result.txt -k "spirit"
$ python main.py --decrypt --input-file "data/ciphertext.txt" --output-file "data/result.txt" --key "spirit"
```

Decrypt text with known key length:
``` bash
$ python main.py -d -i "data/ciphertext.txt" -o "data/result.txt -l 6
$ python main.py --decrypt --input-file "data/ciphertext.txt" --output-file "data/result.txt" --key-len 6
```

Decrypt text with known max key length:
``` bash
$ python main.py -d -i "data/ciphertext.txt" -o "data/result.txt -m 8
$ python main.py --decrypt --input-file "data/ciphertext.txt" --output-file "data/result.txt" --max-key-len 8
```

