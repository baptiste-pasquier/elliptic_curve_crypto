# -*- coding: utf-8 -*-
"""
Signature ECDSA (Elliptic Curve Digital Signature Algorithm)
"""

from .corps_fini import invmod, Courbe, Point
from .ecdh import random_key
import hashlib
import random

import os


def hash_m(message, n):
    """Hachage d'un message
    La longueur binaire du message haché sera inférieure à la 
    longueur binaire de n (voir documentation)

    Args:
        message (string): message à hacher
        n (int): ordre du point G

    Returns:
        int: message haché
    """
    a = hashlib.sha3_512(bytes(message, "utf-8")).digest()
    e = int.from_bytes(a, byteorder='big')
    if e.bit_length() >= n.bit_length():
        z = e >> (e.bit_length() - n.bit_length())
        return z
    else:
        return e


def signature(message, G, n, nA):
    """Signature d'un message par Alice

    Args:
        message (string): message à signer
        G (Point): point générateur d'un sous-groupe
        n (int): ordre du point G
        nA (int): clé privée de Alice

    Returns:
        int, int: signature du message
    """
    r = 0
    s = 0
    while r == 0 or s == 0:
        k = random.randint(1, n - 1)
        x = (k * G).x
        r = x % n
        s = ((hash(message) + r * nA) * invmod(k, n)) % n
    return r, s


def verification(message, PA, rs, G, n):
    """Vérification de la signature du message par Bob

    Args:
        message (string): message dont la signature doit être vérifiée
        PA (Point): clé publique d'Alice
        rs (int, int): signature
        G (Point): point générateur d'un sous-groupe
        n (int): ordre du point G

    Returns:
        bool: True si signature valide, False sinon
    """
    r, s = rs
    if r < 1 or r > (n - 1) or s < 1 or s > (n - 1):
        return False

    u1 = (hash(message) * invmod(s, n)) % n
    u2 = (r * invmod(s, n)) % n
    C = (u1 * G) + (u2 * PA)
    if r == (C.x % n):
        return True
    else:
        return False


def simulationECDSA(p, a, b, g, n, c, message):
    """[summary]

    Args:
        p (int): nombre premier définissant le corps fini Fp
        a (int): coefficient de la courbe elliptique y^2 = x^3 + ax + b
        b (int): coefficient de la courbe elliptique y^2 = x^3 + ax + b
        g (int, int): point G définisant un sous-groupe cyclique
        n (int): ordre du point G
        c (int): nombre de bits des clés privées
        message (string)
    """
    E = Courbe(a, b, p)
    G = Point(E, g[0], g[1])

    # Alice
    nA = random_key(c)                  # Alice génère sa clé privée
    PA = nA * G                         # Alice calcule sa clé publique
    rs = signature(message, G, n, nA)   # Alice signe le message

    # Bob
    verif = verification(message, PA, rs, G, n)

    print("Clé privée d'Alice:", hex(nA))
    print("Clé publique d'Alice:", (hex(PA.x), hex(PA.y)))
    print("Message envoyé par Alice:", message)
    print("Signature valide:", verif)
