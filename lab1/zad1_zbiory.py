# zad1
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {2, 4, 6, 8, 10}
set3 = {1, 3, 5, 7, 9}
set = {0}
set.pop()
# a
for i in set1:
    if i not in set2:
        set.add(i)
for i in set2:
    if i not in set1:
        set.add(i)
print(set)
set.clear()

# b
for i in set2:
    if i not in set1:
        if i not in set3:
            set.add(i)
print(set)
set.clear()

# c
for i in set1:
    if i in set2:
        if i not in set3:
            set.add(i)
    if i in set3:
        if i not in set2:
            set.add(i)
for i in set2:
    if i in set3:
        if i not in set1:
            set.add(i)
print(set)
set.clear()

# d
for i in range(1, 26):
    if i not in set1:
        set.add(i)
print(set)
set.clear()

# e
for i in range(1, 26):
    if i not in set1:
        if i not in set2:
            if i not in set3:
                set.add(i)
print(set)
set.clear()

# f
for i in range(1, 26):
    if i not in set1:
        if i not in set2:
            if i not in set3:
                set.add(i)
print(set)
set.clear()





