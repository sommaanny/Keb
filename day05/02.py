def print_add(*args):
    print(*args)

def add_args(func, *args):
    func(*args)

add_args(print_add, 1, 2, 3, 4, 5)

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(a)
print(b)
print(a())
print(b())
