def print_add(*args):
    print(*args ** 2)

def add_args(func, *args):
    func(*args)

add_args(print_add, 1, 2, 3, 4, 5)

