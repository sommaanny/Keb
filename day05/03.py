even_number = [i for i in range(51) if i % 2 ==0]
print(even_number)
print()
print(tuple(map(lambda x: x**2, even_number)))
print()
# or

z = lambda x: x**2
print(tuple(map(z, even_number)))
print()

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'hiss']
edit_story(stairs, lambda x : x.capitalize() + '!')

# def my_gen():
#     for i in range(3):
#         yield i
# gen = my_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))

gen = (i for i in range(3))
print(next(gen))
print(next(gen))
print(next(gen))
