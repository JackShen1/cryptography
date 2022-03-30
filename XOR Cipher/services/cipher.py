import string
from collections import Counter
from random import randint, sample
from typing import Optional


def shift_byte_arr(byte_arr: bytearray, shift: int) -> bytearray:
    return byte_arr[shift:] + byte_arr[:shift]


def count_matches(origin: bytearray, shifted: bytearray) -> float:
    matches = sum(a == b for a, b in zip(origin, shifted))
    return int(matches / len(origin) * 1000) / 10


def delete_repetitions(
    probable_rep: list[tuple[float, int]]
) -> list[tuple[float, int]]:
    probable_rep.sort(key=lambda len_rep: len_rep[1])
    probable_key_lens = [probable_rep[0]]
    for key_len1 in probable_rep[1:]:
        keep = True
        for key_len2 in probable_key_lens:
            if key_len1[1] % key_len2[1] == 0:
                keep = False
        if keep:
            probable_key_lens.append(key_len1)

    return sorted(probable_key_lens, reverse=True)


def find_key_len(
    ciphertext: bytearray, max_len: Optional[int]
) -> list[tuple[float, int]]:
    if not max_len:
        max_len = 32

    shifted_arrays = [
        shift_byte_arr(ciphertext, shift) for shift in range(1, max_len + 1)
    ]
    matches = sorted(
        [(0.0, 0)]
        + [
            (count_matches(ciphertext, shifted_arrays[shift - 1]), shift)
            for shift in range(1, max_len + 1)
        ],
        reverse=True,
    )

    probable_key_rep = []
    prev_prc = 0
    for match in matches[1:]:
        curr_prc = match[0]
        if curr_prc < prev_prc * 0.8:
            break
        probable_key_rep.append(match)
        prev_prc = curr_prc

    return delete_repetitions(probable_key_rep)


def find_xor_key(
    ciphertext: bytearray, key_len: int, most_common_byte: int = 32
) -> bytearray:
    key = bytearray([0] * key_len)
    for st_idx in range(key_len):
        keyspace_text = [
            ciphertext[idx] for idx in range(st_idx, len(ciphertext), key_len)
        ]
        most_common_found = Counter(keyspace_text).most_common(1)[0][0]
        key[st_idx] = most_common_byte ^ most_common_found
    return key


def encrypt(text: str, key: str) -> bytearray:
    if not key:
        key = "".join(sample(string.ascii_lowercase, randint(5, 10)))

    return bytearray(ord(text[i]) ^ ord(key[i % len(key)]) for i, _ in enumerate(text))


def decrypt(ciphertext: bytearray, key: bytearray) -> bytearray:
    return bytearray(
        ciphertext[i] ^ key[i % len(key)] for i, _ in enumerate(ciphertext)
    )
