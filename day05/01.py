word = "INHA"
test ={}
test2 = {l : word.count(l) for l in word}
for i in word:
    test[i] = word.count(i)


print(test)
print(test2)