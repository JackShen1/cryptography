from math import gcd
from random import randint

from const import SYM_NUM, UA_SYMBOLS


def gen_random_key() -> int:
    while True:
        k1, k2 = randint(2, SYM_NUM), randint(2, SYM_NUM)
        if gcd(k2, SYM_NUM) == 1:
            return k2 * SYM_NUM + k1


def get_all_keys() -> list:
    res = [i for i in range(2, SYM_NUM) if gcd(SYM_NUM, i) == 1]

    return [i * SYM_NUM + k for k in range(2, SYM_NUM) for i in res]


def find_affine_key(ciphertext: str) -> list:
    keys = get_all_keys()
    res = []
    for key in keys:
        out_text = decrypt(decrypt(ciphertext, key), key)

        res.append(f"Key: {str(key)}\nDecrypted text: {''.join(out_text)[:80]}")
    return res


def encrypt(text: str, key: int) -> str:
    k1, k2 = key // SYM_NUM, key % SYM_NUM
    res = [UA_SYMBOLS[(k1 * UA_SYMBOLS.index(i) + k2) % SYM_NUM] for i in text]

    return "".join(res)


def decrypt(ciphertext: str, key: int) -> str:
    k1, k2 = key // SYM_NUM, key % SYM_NUM
    k3 = pow(k1, -1, SYM_NUM)
    res = [UA_SYMBOLS[((UA_SYMBOLS.index(i) - k2) * k3) % SYM_NUM] for i in ciphertext]

    return "".join(res)
