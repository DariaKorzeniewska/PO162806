import numpy as np
A = np.array([[5, 10], [7, 6]])
B = np.array([[2, 3], [1, 9]])
# zad1
def sum(a,b):
    return a+b
sum1 = sum(A,B)
print(sum1)

# zad1 update
M1 = [[2, 5, 7], [2, 7, 9], [1, 2, 3]]
M2 = [[1, 3, 10], [11, 2, 10], [4, 10, 5]]


def sumu(a, b):
    macierz = []
    for x in range(len(a)):
        wiersz = []
        for y in range(len(a[x])):
            wiersz.append(a[x][y] + b[x][y])
        macierz.append(wiersz)
    return macierz

print("Suma ", sumu(M1,M2))


# zad2
def product(a,b):
    return a*b
product1 = product(A,B)
print(product1)

# zad2 update
def productu(a,b):
    macierz = []
    for x in range(len(a)):
        wiersz = []
        for y in range(len(a[x])):
            wiersz.append(a[x][y] * b[y][x])
        macierz.append(wiersz)
    return macierz
print("Product ", productu(M1,M2))

# zad3
def mult(a,x):
    return a*x
mult1 = mult(A,2)
print(mult1)

# zad3 update
def multu(a,w):
    macierz = []
    for x in range(len(a)):
        wiersz = []
        for y in range(len(a[x])):
            wiersz.append(a[x][y]*w)
        macierz.append(wiersz)
    return macierz
print("Mult ", multu(M1,2))

# zad4
C = np.array([[1, 2], [3, 4]])
def transp(a):
    return a.transpose()
transp1 = transp(C)
print(transp1)

# zad4 update
C = [[1, 2], [3, 4]]
def transpu(a):
    macierz = []
    for x in range(len(a)):
        wiersz = []
        for y in range(len(a[x])):
            wiersz.append(a[y][x])
        macierz.append(wiersz)
    return macierz
print("Transp ", transpu(C))





