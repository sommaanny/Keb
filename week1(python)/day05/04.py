def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print("Keyword arguments: ", kwargs)
        result = func(*args, **kwargs)
        print("Result: ", result)
        return result
    return new_function

def add_ints(a, b):
    return a + b
print(add_ints(3, 5))

cooler_add_ints = document_it(add_ints) #데커레이터 수동할당
cooler_add_ints(3, 5)

@document_it
def mul_ints(a, b):
    return a * b
mul_ints(2, 3)

print()
print()
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@square_it
@document_it
def add_int(a, b):
    return a + b
add_int(3, 5)