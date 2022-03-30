from itertools import product
from typing import Generator

from const import EN_SYMBOLS, UA_SYMBOLS


def set_key(ord_key: list, mod: int) -> list:
    arr = list(range(mod))
    j = 0
    for i in range(mod):
        j = (j + arr[i] + ord_key[i % len(ord_key)]) % mod
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def get_stream(arr: list, mod: int) -> Generator:
    i = j = 0
    while True:
        i = (i + 1) % mod
        j = (j + arr[i]) % mod
        arr[i], arr[j] = arr[j], arr[i]
        yield arr[(arr[i] + arr[j]) % mod]


def get_settings(locale: str) -> tuple:
    if locale == "UA":
        mod = 2048
        step = 3
        hex_int = "03X"
    else:
        mod = 256
        step = 2
        hex_int = "02X"

    return mod, step, hex_int


def full_encrypt(text: str, locale: str, key1: str, key2: str) -> str:
    mod = get_settings(locale)[0]
    hex_int = get_settings(locale)[2]
    ord_msg = [ord(i) for i in text]

    enc_1 = encrypt(key1, ord_msg, mod)
    enc_2 = encrypt(key2, enc_1, mod)

    result = [format(i, hex_int) for i in enc_2]

    return "".join(result)


def encrypt(key: str, msg, mod: int) -> list:
    ord_key = [ord(j) for j in key]
    arr = set_key(ord_key, mod)
    stream = get_stream(arr, mod)

    result = [k ^ next(stream) for k in msg]

    return result


def full_decrypt(text: str, locale: str, key1: str, key2: str) -> str:
    mod = get_settings(locale)[0]
    step = get_settings(locale)[1]
    ord_msg = [int(text[i : i + step], 16) for i in range(0, len(text), step)]

    dec_1 = decrypt(key2, ord_msg, mod)
    dec_2 = decrypt(key1, dec_1, mod)

    result = [chr(i) for i in dec_2]

    return "".join(result)


def decrypt(key: str, msg: list, mod: int) -> list:
    ord_key = [ord(j) for j in key]
    arr = set_key(ord_key, mod)
    stream = get_stream(arr, mod)

    result = [k ^ next(stream) for k in msg]

    return result


def bruteforce(msg: str, locale: str) -> str:
    keys1, keys2 = [], []

    mod = get_settings(locale)[0]
    step = get_settings(locale)[1]
    ord_msg = [int(msg[i : i + step], 16) for i in range(0, len(msg), step)]

    for q in range(1, len(ord_msg) + 1):
        for k in range(1, len(ord_msg) + 1):
            if locale == "UA":
                all_chars = set(UA_SYMBOLS)
                keys1, keys2 = product(UA_SYMBOLS, repeat=q), product(
                    UA_SYMBOLS, repeat=k
                )
            else:
                all_chars = set(EN_SYMBOLS)
                keys1, keys2 = product(EN_SYMBOLS, repeat=q), product(
                    EN_SYMBOLS, repeat=k
                )

            for key1 in keys1:
                for key2 in keys2:
                    ord_key1 = [ord(j) for j in key1]
                    arr1 = set_key(ord_key1, mod)
                    stream1 = get_stream(arr1, mod)

                    result = [(j ^ next(stream1)) for j in ord_msg]

                    ord_key2 = [ord(j) for j in key2]
                    arr2 = set_key(ord_key2, mod)
                    stream2 = get_stream(arr2, mod)

                    translated = "".join([chr(c ^ next(stream2)) for c in result])

                    if set(translated).issubset(all_chars):
                        return f"Decrypted text: {''.join(translated)}"

    return "Cannot find original text!"
