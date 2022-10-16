# zad2
tekst2 = "Fauna"
teskt1 = "florA"
s = {0}
s.clear()
# a
def a(l1, l2):
    for i in l1:
        if i in l2:
            s.add(i)
    return s
a1 = a(teskt1, tekst2)
print(a1)
s.clear()

# b
def b(l1, l2):
    s.add(l1)
    s.add(l2)
    return s
b1 = b(teskt1, tekst2)
print(b1)
s.clear()








