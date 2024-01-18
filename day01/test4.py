import sys

T = int(sys.stdin.readline())

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(int(factorial(M) / factorial(M - N) / factorial(N)))
