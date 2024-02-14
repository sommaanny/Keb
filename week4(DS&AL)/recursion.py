
def change_oct(num):
    if num < 8:
        return str(num)
    return change_oct(num // 8) + str(num % 8)
print(change_oct(100))
print('---------------------------')

def fibonacci(number):
    i = 2
    arr = [1, 1]
    if number <= 2:
        return arr[:number]
    prev = fibonacci(number-1)
    return prev + [prev[-2] + prev[-1]]

print(fibonacci(5))