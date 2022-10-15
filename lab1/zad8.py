#zad8
lista = [x for x in range(2, 10000)]
for licznik in range(2, 100):
    for liczba in range(len(lista)):
        if liczba % licznik == 0 and liczba != licznik:
            lista.pop(liczba)

print(lista)





