def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

class Wymierna:
    p = 0
    q = 1
    def __init__(self, p: int, q: int) -> None:
        self.p = p
        self.q = q

    def get_licznik(self):
        return self.p

    def get_mianownik(self):
        return self.q

    def __repr__(self):
        return str(self.p) + "/" + str(self.q)

    def __float__(self):
        return float(self.p/self.q)

    def __add__(self, a, b):
        a *= self.q
        new1 = self.p * b
        new2 = self.q * b
        new1 += a
        dzielnik = nwd(new1, new2)
        new1 /= dzielnik
        new2 /= dzielnik
        return int(new1), int(new2)

    def __sub__(self, a, b):
        a *= self.q
        new1 = self.p * b
        new2 = self.q * b
        new1 -= a
        dzielnik = nwd(new1, new2)
        new1 /= dzielnik
        new2 /= dzielnik
        return int(new1), int(new2)

    def __eq__(self, a, b):
        if self.q == b:
            if self.p == a:
                return True
        return False

    def __ne__(self, a, b):
        return not self.__eq__(a, b)

    def __lt__(self, a, b):  # less than
        a *= self.q
        self.p *= b
        self.q *= b
        b *= self.q

        if self.p < a:
            if self.q < b:
                return True
        return False

    def __le__(self, a, b):  # less or equal
        a *= self.q
        self.p *= b
        self.q *= b
        b *= self.q

        if self.p <= a:
            if self.q <= b:
                return True
        return False

    def __gt__(self, a, b):  # greater than
        return not self.__le__(a, b)

    def __ge__(self, a, b):  # greater or equal
        return not self.__lt__(a, b)

    def __mul__(self, a, b):
        a *= self.p
        b *= self.q
        dzielnik = nwd(a, b)
        a /=dzielnik
        b /=dzielnik
        return a, b

  #  def __div__(self, a, b):



