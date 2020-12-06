from eccrypto.ecdh import simulationECDH
from eccrypto.elgamal import simulationElGamal
from eccrypto.ecdsa import simulationECDSA
from eccrypto.corps_fini import Courbe, Point

# %% Simulation ECDH

# Courbe elliptique P-256 du NIST
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a = -3
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
g = (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)

print("Simulation ECDH\n")
simulationECDH(p, a, b, g, 256)


# %% Simulation ElGamal

# Courbe elliptique P-256 du NIST
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a = -3
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
g = (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)

# Choix d'un message
# Le message doit être codé sous forme d'un point du sous-groupe engendré par G
# Nous prenons par exemple le point 3 * G
E = Courbe(a, b, p)
G = Point(E, g[0], g[1])
m = 5 * G

print("\n\nSimulation ElGamal\n")
simulationElGamal(p, a, b, g, 256, m)


# %% Simulation ECDSA

# # Courbe elliptique secp256k1
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
a = 0
b = 7
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)

message = "Hello"

print("\n\nSimulation ECDSA\n")
simulationECDSA(p, a, b, g, n, 256, message)
