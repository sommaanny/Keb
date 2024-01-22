#8.1
e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
print(e2f)
print()

#8.2
print(e2f['walrus'])
print()

#8.3
f2e = {}
for k, v in e2f.items():
    f2e[v] = k
print(f2e)
print()

#8.4
print(f2e['chien'])

#8.5
print(', '.join(list(e2f.keys())))

#8.6
life = {'animals' : {'cats': 'Henri', 'octopi' : 'Grumpy', 'emus' : 'Lucy'}, 
        'plants' : {} , 'other' : {}}
print(life)

#8.7
print(', '.join(list(life.keys())))

#8.8
print(', '.join(list(life['animals'].keys())))

#8.9
print(life['animals']['cats'])

#8.10
squares = {i : i*i for i in range(10)}
print(squares)