import numpy as np
A = np.array([[5, 10], [7, 6]])
B = np.array([[2, 3], [1, 9]])
# zad1
def sum(a,b):
    return a+b

sum1 = sum(A,B)
print(sum1)

# zad2
def product(a,b):
    return a*b

product1 = product(A,B)
print(product1)

# zad3
def mult(a,x):
    return a*x

mult1 = mult(A,2)
print(mult1)

# zad4
C = np.array([[1,2], [3,4]])

def transp(a):
    return a.transpose()

transp1 = transp(C)
print(transp1)





