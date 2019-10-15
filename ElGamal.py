# -*- coding: utf-8 -*-
"""
chiffrement de ElGamal
"""

from Corpsfini import Courbe, Point
import os


def générateur(c):
    """Renvoie une clé aléatoire de c bits sous forme hexadecimal"""
    a = os.urandom(c // 8)
    return (int.from_bytes(a, byteorder='big'))


def simulation(p, a, b, g, c, m):
    E = Courbe(a, b, p)
    G = Point(E, g[0], g[1])
    m = 3 * G

    # Bob
    y = 100     		  # Bob génère sa clé privée
    Y = y * G             # Bob calcule sa clé publique

    # Alice
    k = 50     			  # Alice génère un aléa k
    A = k * G             # Alice calcule A
    B = m + k * Y         # ALice calcule B à partir de Y

    # Bob
    Pb = y * A            # Bob calcule P' à partir de A
    mb = B + (-Pb)        # Bob calcule m' à partir de B

    print("Message envoyé par Alice:", (hex(m.x), hex(m.y)))
    print("Message déchiffré par Bob:", (hex(mb.x), hex(mb.y)))


p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a = -3
n = 115792089210356248762697446949407573529996955224135760342
422259061068512044369
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
g = (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
