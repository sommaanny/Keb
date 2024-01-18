#8.11
odd_set = {i for i in range(10) if i % 2 != 0}
print(odd_set)

#8.12
gen = (i for i in "Got")
gen2 = (j for j in range(10))
for _ in gen:
    print(_, end='')
print()
for _ in gen2:
    print(_, end=' ')
print()

#8.13
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?') 
dic_test = dict(zip(keys, values))
print(dic_test)

#8.14
titles = ['Creauture of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)

dic_test2 = {(1, 2) : 'o' , (3, 4) : 'x'}
print(dic_test2)