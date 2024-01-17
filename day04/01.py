import copy

list_a = [1, 2, 3]
list_b = list_a
list_c = list_a.copy()
list_d = list_a[:]
print(list_a, list_b, list_c, list_d)
print()
list_a.append(4)
print(list_a, list_b, list_c, list_d)
print()

for a, b in zip(list_a, list_b):
    print(a, b)

dic_a = {'1': 'a', '2': 'b'}
for key, value in dic_a.items():
    print(key, ":", value)

list_test = [i for i in range(1, 11) if i % 2 == 0]
print(list_test)

a = 4
b = copy.deepcopy(a)
print(a, b)
a = 3
print(a, b)
print()

dic_b = dic_a
dic_c = dic_a.copy()
dic_d = copy.deepcopy(dic_a)
print(dic_a, dic_b, dic_c, dic_d)