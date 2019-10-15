# -*- coding: utf-8 -*-
"""
Signature ECDSA (Elliptic Curve Digital Signature Algorithm)
"""

from Corpsfini import invmod, Courbe, Point
import hashlib
import random

import os

p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
a = 0
b = 7
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)


E = Courbe(a, b, p)
G = Point(E, g[0], g[1])


def générateur(c):
    """Renvoie une clé aléatoire de c bits sous forme hexadecimal"""
    a = os.urandom(c // 8)
    return (int.from_bytes(a, byteorder='big'))


def créationclés(c):
    nA = générateur(c)   # Alice génère sa clé privée
    PA = nA * G          # Alice calcule sa clé publique
    return(nA, PA)


def hash(message):
    a = hashlib.sha3_512(bytes(message, "utf-8")).digest()
    e = int.from_bytes(a, byteorder='big')
    if e.bit_length() >= n.bit_length():
        z = e >> (e.bit_length() - n.bit_length())
        return(z)
    else:
        return(e)


def signature(message):
    r = 0
    s = 0
    while r == 0 or s == 0:
        k = random.randint(1, n - 1)
        x = (k * G).x
        r = x % n
        s = ((hash(message) + r * nA) * invmod(k, n)) % n
    return(r, s)


def vérification(PA, message, r, s):
    if r < 1 or r > (n - 1) or s < 1 or s > (n - 1):
        return("Signature invalide")

    u1 = (hash(message) * invmod(s, n)) % n
    u2 = (r * invmod(s, n)) % n
    C = (u1 * G) + (u2 * PA)
    if r == (C.x % n):
        return("Signature valide")
    else:
        return("Signature invalide")
