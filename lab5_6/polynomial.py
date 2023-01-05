# do zadniania 4 ---- nobione na lekcji
from __future__ import annotations #do wstawienia -> Polynomial
class Polynomial:
    __coefficients: list  #zmienna prywatna niewidoczna z poziomu main

    def __init__(self, coefficients: list) -> None:
        if len(coefficients) == 0:
            print('lista nie powinna byc pusta')
            exit(1)

        self.__coefficients = coefficients

    @property   #pobieranie wartosci pola
    def coefficients(self) -> list:
        return self.__coefficients      #metoda ukryta tworzy dostęp do zmiennej prywatnej

    @coefficients.setter    #metoda ukryta do ustawiania nowej listy
    def coefficients(self, coef: list) -> None:
        if len(coef) == 0:
            print('lista nie powinna byc pusta')
            exit(1)
        self.__coefficients = coef

    def deg(self):
        return len(self.__coefficients) - 1

    def __neg__(self) -> Polynomial:
        new_coef = []
        for i in self.__coefficients:
            new_coef.append((-1)*i)
        return Polynomial(new_coef)

    def __add__(self, other_poly):
        new_poly = []
        for i in other_poly:
            new_poly = self.__coefficients[i] + other_poly[i]

        while new_poly[0] == 0:
            new_poly.pop(0)


        return new_poly

a = Polynomial([3, 2, 1])
print(a.coefficients)
a.coefficients = [5, 0, 3, 2, 1]
print(a.coefficients)
b = -a
print(b.coefficients)