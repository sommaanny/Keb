import sys
import math

# n = int(sys.stdin.readline())

# for i in range(2, int(math.sqrt(n)) + 1):
#     if n % i == 0:
#         print("Not 소수")
#         break
# else:
#     if (n > 2):
#         print("소수")
#     else:
#         print("Not 소수")

M, N = map(int, sys.stdin.readline().split())

if M > N:
    tmp = M
    M = N
    N = tmp

list_prime = [1 for i in range(N + 1)]
list_prime[0] = 0
list_prime[1] = 0
for j in range(2, int(math.sqrt(N)) + 1):
    if list_prime[j] == 1:
        k = 2
        while(j * k <= N):
            list_prime[j * k] = 0
            k += 1

for w in range(M, N + 1):
    if list_prime[w] == 1:
        print(w, end=' ')