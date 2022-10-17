# zad1
a = [a for a in range(1, 11)]
b = [b*b for b in range(1, 11)]
c = [c*c*c for c in range(1, 11)]
tab = [a, b, c]
print(tab)

# zad2
tab2 = []
for i in range(1, 11):
    d = [d for d in range(1, i+1)]
    suma = 0
    for j in d:
        suma += j
    print(suma)
    tab2.append(d)
print(tab2)




