#zad1
lista = []
#a
for i in range(1,11):
    lista.append(i)
print(lista)
lista.clear()
#b
for i in range(0,11):
    lista.append(i*2)
print(lista)
lista.clear()
#c
for i in range(1,11):
    lista.append(i*i)
print(lista)
lista.clear()
#d
for i in range(10):
    lista.append(0)
print(lista)
lista.clear()
#e
for i in range(1,11):
    if i%2==0:
        lista.append(1)
    if i%2!=0:
        lista.append(0)
print(lista)
lista.clear()
#f
for i in range(2):
    for j in range(5):
        lista.append(j)
print(lista)
lista.clear()

print("----------------------------------------")
#zad2
#a
a=1
while a!=11:
    lista.append(a)
    a+=1
print(lista)
lista.clear()
#b
a=0
while a!=12:
    lista.append(a*2)
    a+=1
print(lista)
lista.clear()
#c
a=1
while a!=11:
    lista.append(a*a)
    a+=1
print(lista)
lista.clear()
#d
a=1
while a!=11:
    lista.append(0)
    a+=1
print(lista)
lista.clear()
#e
a=1
while a!=11:
    if a%2==0:
        lista.append(1)
    else:
        lista.append(0)
    a+=1
print(lista)
lista.clear()
#f
a=1
b=0
while a!=3:
    b=0
    while b!=5:
        lista.append(b)
        b+=1
    a+=1
print(lista)
lista.clear()


