import time

import matplotlib.pyplot as plt

import rsa


def make_plot(fr: int, to: int, ax: list):
    plt.plot(range(fr, to), ax)
    plt.show()


def encrypt_test():
    y = []
    for i in range(1, 101):
        pb, pr = rsa.newkeys(1024)
        t1 = time.time()
        rsa.encrypt(bytes("a" * i, "utf-8"), pb)
        t2 = time.time()
        y.append(t2 - t1)
    return y


def decrypt_test():
    y = []
    for i in range(1, 101):
        pb, pr = rsa.newkeys(1024)
        enc = rsa.encrypt(bytes("a" * i, "utf-8"), pb)
        t1 = time.time()
        rsa.decrypt(enc, pr)
        t2 = time.time()
        y.append(t2 - t1)
    return y


make_plot(1, 101, encrypt_test())
make_plot(1, 101, decrypt_test())
