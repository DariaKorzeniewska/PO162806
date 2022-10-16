#zad7
lista=[]
number=int(input("Podaj pierwsza liczbe: "))
lista.append(number)
i = 0
while i < 9:
    number = int(input("Podaj liczbe: "))
    if number not in lista:
        lista.append(number)
        i += 1
    else:
        print("Podaj inną liczbę !")

print("Twoja lista: ", lista)







