# -*- coding: utf-8 -*-
"""
chiffrement de ElGamal
"""

from .corps_fini import Courbe, Point
from .ecdh import random_key


def simulationElGamal(p, a, b, g, c, m):
    """Simulation d'un chiffrement de ElGamal

    Args:
        p (int): nombre premier définissant le corps fini Fp
        a (int): coefficient de la courbe elliptique y^2 = x^3 + ax + b
        b (int): coefficient de la courbe elliptique y^2 = x^3 + ax + b
        g (int, int): point G définisant un sous-groupe cyclique
        c (int): nombre de bits des clés privées
        m (Point): le message doit être codé sous forme d'un point du sous-groupe engendré par G
    """
    E = Courbe(a, b, p)
    G = Point(E, g[0], g[1])

    # Bob
    y = random_key(c)     # Bob génère sa clé privée
    Y = y * G             # Bob calcule sa clé publique

    # Alice
    k = random_key(c)	  # Alice génère un aléa k
    A = k * G             # Alice calcule A
    B = m + k * Y         # ALice calcule B à partir de Y

    # Bob
    Pb = y * A            # Bob calcule P' à partir de A
    mb = B + (-Pb)        # Bob calcule m' à partir de B

    print("Message envoyé par Alice:", (hex(m.x), hex(m.y)))
    print("Message déchiffré par Bob:", (hex(mb.x), hex(mb.y)))
