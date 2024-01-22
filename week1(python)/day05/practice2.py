#9.1
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

#9.2
def get_odds():
    for i in range(10):
        if i % 2 != 0:
            yield i
gen = get_odds()
for _ in range(3):
    next(gen)
    if _ == 1:
        print(next(gen))

gen2 = (i for i in range(10) if i % 2 == 1)
for _ in range(3):
    next(gen2)
    if _ == 1:
        print(next(gen2))

#9.3
def test(func):
    def new_function(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        return print("end")
    return new_function

@test
def k():
    print("ooo")
k()

#9.4
class OopsException(Exception):
    pass
try:
    raise OopsException
except OopsException:
    print("Caught an oops")