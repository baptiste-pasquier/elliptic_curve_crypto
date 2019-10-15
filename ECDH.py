# -*- coding: utf-8 -*-
"""
Echange de clés de Diffie-Hellman (Elliptic Curve Diffie-Hellman)
"""

from Corpsfini import Courbe, Point
import os


def générateur(c):
    """Renvoie une clé aléatoire de c bits sous forme hexadecimal"""
    a = os.urandom(c // 8)
    return (int.from_bytes(a, byteorder='big'))


def simulation(p, a, b, g, c):
    E = Courbe(a, b, p)
    G = Point(E, g[0], g[1])

    # Alice
    nA = générateur(c)     # Alice génère sa clé privée
    PA = nA * G            # Alice calcule sa clé publique

    # Bob
    nB = générateur(c)     # Bob génère sa clé privée
    PB = nB * G            # Bob calcule sa clé publique

    # Alice
    KA = nA * PB           # Alice calcule la clé secrète à partir de PB

    # Bob
    KB = nB * PA           # Bob calcule la clé secrète à partir de PA

    print("Clé privée d'Alice:", hex(nA))
    print("Clé publique d'Alice:", (hex(PA.x), hex(PA.y)))
    print("Clé privée de Bob:", hex(nB))
    print("Clé publique de Bob:", (hex(PB.x), hex(PB.y)))
    print("Clé secrète d'Alice:", (hex(KA.x), hex(KA.y)))
    print("Clé secrète de Bob:", (hex(KB.x), hex(KB.y)))


p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a = -3
n = 115792089210356248762697446949407573529996955224135760342
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
g = (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
