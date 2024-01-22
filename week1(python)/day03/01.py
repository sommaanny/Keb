test = "Hello"
print(test)
test = test.replace('H', 'K')
print(test)
test = 'H' + test[1:]
print(test)

print()

test2 = "AAABBBCCC"
print(test2)
test2 = test2.replace('A', 'K', 2)
print(test2)

test3 = "What! the...!!?"
print(test3.strip(".!?"))
print(test3.replace('!', '').replace('.', '').replace('?', ''))

d = {'a' : 'apple', 'b' : 'banana'}
print("{0[a]}, {0[b]}".format(d))
print(d['a'])