import time

import matplotlib.pyplot as plt
from ellipticcurve import Ecdsa, PrivateKey


def gen_sign(msg: str, pr_key):
    return Ecdsa.sign(msg, pr_key)


def verify(msg: str, sign, pb_key):
    return Ecdsa.verify(msg, sign, pb_key)


def make_plot(fr: int, to: int, ax: list, by: int = 1):
    plt.plot(range(fr, to, by), ax)
    plt.show()


def encrypt_test():
    y = []
    for i in range(1, 200):
        pr = PrivateKey()
        t1 = time.time()
        gen_sign("a" * i, pr)
        t2 = time.time()
        y.append(t2 - t1)
    return y


def decrypt_test():
    y = []
    for i in range(1, 200):
        pb, pr = PrivateKey().publicKey(), PrivateKey()
        signature = gen_sign("a" * i, pr)
        t1 = time.time()
        verify("a" * i, signature, pb)
        t2 = time.time()
        y.append(t2 - t1)
    return y


make_plot(1, 200, encrypt_test())
make_plot(1, 200, decrypt_test())
