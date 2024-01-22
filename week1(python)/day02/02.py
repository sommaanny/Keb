a = 7
print(isinstance(a, int))
print()
b = a
print(a)
print(b)
b = 99
print(a)
print(b)  # inmutable type

list_a = [1, 2, 3]
list_b = list_a
print(list_a)
print(list_b)
list_b[0] = 99
print(list_a)
print(list_b)   #mutable한 type
print()