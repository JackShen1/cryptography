import time

import matplotlib.pyplot as plt
from services.cipher import decrypt, encrypt, find_affine_key, get_all_keys


def make_plot(fr: int, to: int, ax: list):
    plt.plot(range(fr, to), ax)
    plt.show()


all_keys = get_all_keys()


def test_enc_1():
    y = []
    for i in range(2, 500):
        t1 = time.time()
        encrypt(encrypt("ї" * i, 1234), 1234)
        t2 = time.time()
        y.append(t2 - t1)
    return y


make_plot(2, 500, test_enc_1())


def test_enc_2():
    res = []
    for i in range(2, len(all_keys), 5):
        t1 = time.time()
        encrypt(encrypt("ї" * 200, all_keys[i]), all_keys[i])
        t2 = time.time()
        res.append(t2 - t1)
    return res


plt.plot(range(2, len(all_keys), 5), test_enc_2())
plt.show()


def test_dec_1():
    res = []
    for i in range(2, 500):
        t1 = time.time()
        decrypt(decrypt("ї" * i, 1234), 1234)
        t2 = time.time()
        res.append(t2 - t1)
    return res


make_plot(2, 500, test_dec_1())


def test_dec_2():
    res = []
    for i in range(2, len(all_keys), 5):
        t1 = time.time()
        decrypt(decrypt("є" * 200, all_keys[i]), all_keys[i])
        t2 = time.time()
        res.append(t2 - t1)
    return res


plt.plot(range(2, len(all_keys), 5), test_dec_2())
plt.show()


def test_hack():
    res = []
    for i in range(2, 500):
        t1 = time.time()
        find_affine_key("ї" * i)
        t2 = time.time()
        res.append(t2 - t1)
    return res


make_plot(2, 500, test_hack())
