# zad1

from array import *
print(array.__dict__)

# zad2
class klasa_dict:
    def __init__(self, jakas_zmienna):
        self.jakas_zmienna = jakas_zmienna
print(klasa_dict.__dict__)

# zad3
klasa_dict1 = klasa_dict(5)
print(klasa_dict1.__dict__)

# zad5
class Student:
    def __init__(self, nazwa_ucznia, klasa_ucznia, student_id):
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id

    def __str__(self):
        return (f'\nImie i nazwisko: {self.nazwa_ucznia}\n'
                f'Klasa: {self.klasa_ucznia}\n'
                f'ID studenta: {self.student_id}\n')

    # zad6
    def student_data(self, nazwa_lub_klasa = None):
        if nazwa_lub_klasa == self.nazwa_ucznia:
            return self.nazwa_ucznia
        if nazwa_lub_klasa == self.klasa_ucznia:
            return self.klasa_ucznia
        return self.student_id


Student1 = Student('Adam Całkiem', '3A', 123968)
print(Student1)

print(Student1.student_data('Adam Całkiem'))
print(Student1.student_data('3A'))
print(Student1.student_data())

# zad7
print(type(Student))
print(Student.__dict__)
print(Student.__module__)

from array import *

# zad8
class Student:
    def __init__(self):
        None
class Marks:
    def __init__(self):
        None
Student1 = Student()
Student2 = Student()
Student3 = Student()
Marks1 = Marks()
Marks2 = Marks()
Marks3 = Marks()

if Student1.__class__ is Student:
    print('Tak')
if Student2.__class__ is Student:
    print('Tak')
if Student3.__class__ is Student:
    print('Tak')
if Marks1.__class__ is Marks:
    print('Tak')
if Marks2.__class__ is Marks:
    print('Tak')
if Marks3.__class__ is Marks:
    print('Tak')

if isinstance(Student, object) is True:
    print('\nTak')
if isinstance(Marks, object) is True:
    print('Tak')
