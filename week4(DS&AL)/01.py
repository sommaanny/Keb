def fact(n):
    base = 1
    for i in range(n):
        base = base * n
        n -= 1
    return base

def comb(n, r):
    result = fact(n) // (fact(n-r) * fact(r))
    return result

print(comb(4,2))