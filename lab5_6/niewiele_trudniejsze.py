# niewiele trudniejsze
# zad1
class String_class:
    def __init__(self, napis=None):
        self.napis = napis

    def get_string(self, napis):
        self.napis = napis

    def print_string(self):
        print(self.napis.upper())

napis = String_class()
napis.get_string("male lterki")
napis.print_string()

# zad2
class Rectangle:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def pole_prostokata(self):
        return self.dlugosc*self.szerokosc

prosty = Rectangle(2,4)
print(prosty.pole_prostokata())

# zad3
import numpy as np
class Circle:
    def __init__(self, promien):
        self.promien = promien

    def pole_kola(self):
        return np.pi*self.promien*self.promien

    def obwod_kola(self):
        return 2*np.pi*self.promien

kolo = Circle(3)
print(kolo.pole_kola())
print(kolo.obwod_kola())

# zad4
print(f"nazwa klasy instancji kolo to ", kolo.__class__.__name__)

