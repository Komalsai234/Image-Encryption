import secrets
import math
from ecc_constant.curves import *


def gen_key(n):

    key = 0
    while (key == 0):
        key = secrets.randbelow(n)
    return key


def point_add(xp, yp, xq, yq, p, a):
    if xp is None and yp is None:
        return xq, yq
    if xq is None and yq is None:
        return xp, yp

    if xp == xq:
        m = ((3 * (xp**2) + a) * pow(2 * yp, -1, p)) % p
    else:
        m = ((yq - yp) * pow(xq - xp, -1, p)) % p

    xr = (m**2 - xp - xq) % p
    yr = (m*(xp - xr) - yp) % p

    return xr, yr


def point_double(x, y, p, a):
    return point_add(x, y, x, y, p, a)


def montgomery_ladder(pointG, prikey, p, a):
    r0 = (pointG[0], pointG[1])
    r1 = point_double(r0[0], r0[1], p, a)
    bits = bin(prikey)[3:]

    for i in bits:
        if i == '0':
            r1 = point_add(r0[0], r0[1], r1[0], r1[1], p, a)
            r0 = point_double(r0[0], r0[1], p, a)
        else:
            r0 = point_add(r0[0], r0[1], r1[0], r1[1], p, a)
            r1 = point_double(r1[0], r1[1], p, a)

    return r0


class Weierstrass:

    def __init__(self, p: int, a: int, b: int):
        delta = 4*a**3 + 27*b**2
        if delta == 0:
            raise ValueError("Invalid curve parameters")
        self.p = p
        self.a = a
        self.b = b

    def multiply(self, pointG: tuple, prikey: int):
        if (pointG[1]**2) % self.p != (pointG[0]**3 + self.a*pointG[0] + self.b) % self.p:
            raise Exception("parameters do not satisfy equation")

        if prikey == 0:
            return (None, None)

        return montgomery_ladder(pointG, prikey, self.p, self.a)


class Curve:
    def __init__(self, curve=Secp521r1):
        self.curve = curve

    def get_prikey(self, pri_k=0):
        if pri_k == 0:
            self.pri_k = gen_key(self.curve.n)
        else:
            self.pri_k = pri_k
        if self.pri_k >= self.curve.n:
            raise ValueError("Private key must be less than curve order")

    def get_pubkey(self, pri_k=None):
        if pri_k is not None:
            self.pri_k = pri_k

        weierstrass = Weierstrass(self.curve.p, self.curve.a,
                                  self.curve.b)
        self.pub_k = weierstrass.multiply(self.curve.G, self.pri_k)
