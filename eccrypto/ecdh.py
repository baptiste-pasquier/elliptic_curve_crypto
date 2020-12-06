# -*- coding: utf-8 -*-
"""
Echange de clés de Diffie-Hellman (Elliptic Curve Diffie-Hellman)
"""

from .corps_fini import Courbe, Point
import os


def random_key(c):
    """"Renvoie une clé aléatoire de c bits sous forme hexadecimal

    Args:
        c (int): nombre de bits de la clé

    Returns:
        int: clé aléatoire
    """

    a = os.urandom(c // 8)
    return (int.from_bytes(a, byteorder='big'))


def simulationECDH(p, a, b, g, c):
    """Simulation d'un échange de clés ECDH

    Args:
        p (int): nombre premier définissant le corps fini Fp
        a (int): coefficient de la courbe elliptique y^2 = x^3 + ax + b
        b (int): coefficient de la courbe elliptique y^2 = x^3 + ax + b
        g (int, int): point G définisant un sous-groupe cyclique
        c (int): nombre de bits des clés privées
    """
    E = Courbe(a, b, p)
    G = Point(E, g[0], g[1])

    # Alice
    nA = random_key(c)     # Alice génère sa clé privée
    PA = nA * G            # Alice calcule sa clé publique

    # Bob
    nB = random_key(c)     # Bob génère sa clé privée
    PB = nB * G            # Bob calcule sa clé publique

    # Alice
    KA = nA * PB           # Alice calcule la clé secrète à partir de PB

    # Bob
    KB = nB * PA           # Bob calcule la clé secrète à partir de PA

    print("Clé privée d'Alice:", hex(nA))
    print("Clé publique d'Alice:", (hex(PA.x), hex(PA.y)))
    print("Clé privée de Bob:", hex(nB))
    print("Clé publique de Bob:", (hex(PB.x), hex(PB.y)))
    print("Clé secrète calculée par Alice:", (hex(KA.x), hex(KA.y)))
    print("Clé secrète calculée par Bob:", (hex(KB.x), hex(KB.y)))
