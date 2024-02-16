
def change_oct(num):
    if num < 8:
        return str(num)
    return change_oct(num // 8) + str(num % 8)
print(change_oct(100))
print('---------------------------')
count1 = 0
def fibonacci(number):
    global count1
    count1 += 1
    arr = [1, 1]
    if number <= 2:
        return arr[:number]
    result = fibonacci(number-1)
    return result + [result[-2] + result[-1]]

print(fibonacci(31)[-1])
print(count1)
print('----------------------------')
count2 = 0
memo = [None for _ in range(100)]
def fibonacci_memo(n, memo):
    global count2
    count2 += 1
    if memo[n] is not None:
        return memo[n]
    if n < 2:
        return n
    else:
        result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    memo[n] = result
    return result
print(fibonacci_memo(31, memo))
print(count2)
