# -*- coding: utf-8 -*-

""" Implémentation des courbes elliptiques dy type y^2 = x^3 + ax + b sur des corps premiers finis"""


def invmod(a, p):
    """
    Inverse modulaire
    """
    if p == 0:
        raise Exception("p=0")

    c, d = a, p  # Copies

    u1, v1 = 1, 0
    u2, v2 = 0, 1
    r1, r2 = c, d

    while r2 != 0:
        q = r1 // r2
        u = u1
        v = v1
        u1, v1 = u2, v2
        u2, v2 = u - q * u2, v - q * v2
        r1, r2 = r2, r1 - q * r2

    assert r1 == 1
    assert (a * u1) % p == 1

    return u1 % p


class Courbe(object):
    """Courbe elliptique sur un corps premier fini"""

    def __init__(self, a, b, p):
        """Initialisation"""
        self.a = a
        self.b = b
        self.p = p

        self.discriminant = -16 * (4 * a ** 3 + 27 * b ** 2)

        if self.estsinguliere():
            raise Exception("La courbe est singulière")

    def possede_point(self, x, y):
        """Renvoie True si le point est sur la courbe"""
        return ((y**2) - (x**3 + self.a * x + self.b)) % self.p == 0

    def estsinguliere(self):
        """Renvoie True si la courbe est non singulière"""
        return self.discriminant % self.p == 0

    def __eq__(self, autre):
        """Egalité"""
        return(self.a, self.b, self.p) == (autre.a, autre.b, autre.p)

    def __repr__(self):
        """Représentation"""
        return "y^2 = x^3 + {}x + {}  mod {}".format(self.a, self.b, self.p)


class Point(object):
    def __init__(self, courbe, x, y):
        """Initialisation"""
        self.courbe = courbe
        self.x = x
        self.y = y
        self.p = self.courbe.p

        if not self.courbe.possede_point(x, y):
            raise ValueError("Le point {} n'est pas sur la courbe {}".format(self, self.courbe))

    def __repr__(self):
        """Représentation"""
        return "({},{})".format(self.x, self.y)

    def __eq__(self, autre):
        """Egalité"""
        return (self.courbe, self.x, self.y) == (autre.courbe, autre.x, autre.y)

    def __neg__(self):
        """Point opposé"""
        return Point(self.courbe, self.x, (- self.y) % self.p)

    def __add__(self, autre):
        """Addition"""
        assert self.courbe == autre.courbe

        if isinstance(autre, Infini):  # Point infini
            return self

        xs, ys, xa, ya = self.x, self.y, autre.x, autre.y

        if xs == xa:
            if ys != ya:   # Points opposés:
                return Infini(self.courbe)

            if ys == 0:     # ya = 0 aussi
                return Infini(self.courbe)
            else:   # Méthode tangente
                Lambda = (3 * xs ** 2 + self.courbe.a) * invmod(2 * ys, self.p)

        else:  # Cas où xs != xa
            Lambda = (ya - ys) * invmod(xa - xs, self.p)

        x = (Lambda ** 2 - xs - xa) % self.p
        y = (Lambda * (xs - x) - ys) % self.p

        return Point(self.courbe, x, y)

    def __mul__(self, n):
        """Multiplication par un entier"""
        if not isinstance(n, int):
            raise Exception("La multiplication requiert un entier")
        else:
            if n < 0:
                return -self * -n
            if n == 0:
                return Infini(self.courbe)
            else:
                result = Infini(self.courbe)
                q = n
                puiss = self
                while q != 0:
                    if q % 2 == 1:   # si q impair
                        result = result + puiss
                    puiss = puiss + puiss
                    q = q // 2
                return result

    __rmul__ = __mul__


class Infini(object):
    def __init__(self, courbe):
        """Initilisation"""
        self.courbe = courbe

    def __repr__(self):
        return "Infini"

    def __eq__(self, autre):
        """Egalité"""
        return isinstance(autre, Infini)

    def __neg__(self):
        """Point opposé"""
        return self

    def __add__(self, autre):
        """Addition"""
        return autre

    def __mul__(self, n):
        return self

    __rmul__ = __mul__
