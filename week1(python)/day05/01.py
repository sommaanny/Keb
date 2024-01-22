def isPrime(n) -> bool:
    """
    parameters = digit number
    return = bool
    if n == prime -> return True
    else -> return False
    """
    if n < 2:
        return False
    i = 2
    while(i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True
    
def print_data(data,*,start=0, end=100):
    for value in data[start:end]:
        print(value)
    
data = ['a', 'b', 'c', 'd', 'e']
print_data(data, start=1)
print()

