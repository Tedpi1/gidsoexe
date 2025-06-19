my_set = {1, 4, 6, 4, 3, 6, 6, 2, 3, 5, 1, 2, 3, 4, 5}
print("My Set", my_set)

my_set.add(7)
print("After Adding:", my_set)


my_set.discard(3)
print("After Discarding:", my_set)


a = {1, 2, 3}
b = {4, 5, 2}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", b - a)
