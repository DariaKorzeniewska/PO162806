#zad3
def ile_ujemnych(lista):
    ile=0
    for liczba in lista:
        if liczba <0:
            ile+=1
    return(ile)

lista1=[-1,2,3,-4,2,-10,2,6,78,0]
ile1=ile_ujemnych(lista1)
print(ile1)

#zad4
def iloczyn(lista):
    m=1
    for liczba in lista:
        m=m*liczba
    return m

lista2=[2,4,-1]
iloczyn1=iloczyn(lista2)
print(iloczyn1)

#zad5
def minmax(lista):
    min=lista[0]
    max=lista[0]
    for liczba in lista:
        if liczba>max:
            max=liczba
        if liczba<min:
            min=liczba
    krotka=(min,max)
    return krotka

lista3=[1,2,3,4,5,8,0]
minmax1=minmax(lista3)
print(minmax1)

#zad6
def plusMinus(lista):
    i=1
    pm=0
    for liczba in lista:
        if i%2==0:
            pm=pm-liczba
        else:
            pm=pm+liczba
        i+=1
    return pm

lista4=[1,4,16,9,9,7,4,9,11]
plusMinus1=plusMinus(lista4)
print(plusMinus1)












