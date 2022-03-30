import time

import matplotlib.pyplot as plt
from const import DEFAULT_EN_KEYS, DEFAULT_UA_KEYS
from services.cipher import bruteforce, full_decrypt, full_encrypt


def make_plot(fr: int, to: int, ax: list):
    plt.plot(range(fr, to), ax)
    plt.show()


def en_encrypt_test():
    y = []
    for elem in range(1, 100):
        t1 = time.time()
        full_encrypt("j" * elem, "EN", *DEFAULT_EN_KEYS)
        t2 = time.time()
        y.append(t2 - t1)
    return y


def en_double_encrypt_test():
    y = []
    for elem in range(1, 100):
        for j in range(1, 100):
            t1 = time.time()
            full_encrypt("j" * 100, "EN", "a" * elem, "b" * j)
            t2 = time.time()
            y.append(t2 - t1)
    return y


def en_decrypt_test():
    y = []
    for elem in range(1, 100):
        t1 = time.time()
        full_decrypt("b" * elem, "EN", *DEFAULT_EN_KEYS)
        t2 = time.time()
        y.append(t2 - t1)
    return y


def en_double_decrypt_test():
    y = []
    for elem in range(1, 100):
        for j in range(1, 100):
            t1 = time.time()
            full_decrypt("b" * 100, "EN", "a" * elem, "b" * j)
            t2 = time.time()
            y.append(t2 - t1)
    return y


def ua_encrypt_test():
    y = []
    for elem in range(1, 100):
        t1 = time.time()
        full_encrypt("ї" * elem, "UA", *DEFAULT_UA_KEYS)
        t2 = time.time()
        y.append(t2 - t1)
    return y


def ua_double_encrypt_test():
    y = []
    for elem in range(1, 100):
        for j in range(1, 100):
            t1 = time.time()
            full_encrypt("ї" * 100, "UA", "ї" * elem, "і" * j)
            t2 = time.time()
            y.append(t2 - t1)
    return y


def ua_decrypt_test():
    y = []
    for elem in range(1, 100):
        t1 = time.time()
        full_decrypt("7" * elem, "UA", *DEFAULT_UA_KEYS)
        t2 = time.time()
        y.append(t2 - t1)
    return y


def ua_double_decrypt_test():
    y = []
    for elem in range(1, 100):
        for j in range(1, 100):
            t1 = time.time()
            full_decrypt("7" * 100, "UA", "ї" * elem, "і" * j)
            t2 = time.time()
            y.append(t2 - t1)
    return y


def test_hack():
    res = []
    for i in range(1, 100):
        t1 = time.time()
        bruteforce("f" * i, "EN")
        t2 = time.time()
        res.append(t2 - t1)
    return res


make_plot(1, 100, en_encrypt_test())
make_plot(1, 100, ua_encrypt_test())
make_plot(1, 100, en_decrypt_test())
make_plot(1, 100, ua_decrypt_test())

en_double_encrypt = en_double_encrypt_test()
ua_double_encrypt = ua_double_encrypt_test()
en_double_decrypt = en_double_decrypt_test()
ua_double_decrypt = ua_double_decrypt_test()

make_plot(1, len(en_double_encrypt) + 1, en_double_encrypt)
make_plot(1, len(ua_double_encrypt) + 1, ua_double_encrypt)
make_plot(1, len(en_double_decrypt) + 1, en_double_decrypt)
make_plot(1, len(ua_double_decrypt) + 1, ua_double_decrypt)

make_plot(1, 100, test_hack())
