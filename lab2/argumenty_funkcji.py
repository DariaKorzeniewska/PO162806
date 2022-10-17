# zad1
def mult(a):
    iloczyn = 1
    for liczba in a:
        iloczyn=iloczyn*liczba
    return iloczyn

mult1 = mult([3, 5, 7])
print(mult1)
mult2 = mult(range(2, 8, 2))
print(mult2)

# zad2
def mult_ints(*a):
    iloczyn = 1
    for b in a:
        for liczba in b:
            if isinstance(liczba, int) == True:
                iloczyn = iloczyn*liczba
    return iloczyn

mult_ints1 = mult_ints([3, 3.14, 5, "abc", 7])
print(mult_ints1)

# zad3
def multiply(*a):
    iloczyn = 1
    for liczba in a:
        iloczyn *= liczba
    return iloczyn

multiply1 = multiply(3, 5, 7)
print(multiply1)

# zad4
def multiply_ints(*a):
    iloczyn = 1
    for liczba in a:
        if isinstance(liczba,int) == True:
            iloczyn *= liczba
    return iloczyn

multiply_ints1 = multiply_ints(3, 3.14, 5, "abc", 7)
print(multiply_ints1)

# zad5
def make_car(firma, model, a):
    slownik = {"firma" : firma, "model" : model}
    slownik.update(a)
    return slownik

slow = {"kolor": "cafe mocca", "poj_silnika": 900}
make_car1 = make_car("Kia", "Picanto", slow)
print(make_car1)





