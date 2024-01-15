import sys

def gcd(a, b):
    case = [a,b]
    a = max(case)
    b = min(case)
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

N = int(sys.stdin.readline())
list_N = []
for i in range(N):
    list_N.append(int(sys.stdin.readline()))

list_dis = []
for j in range(len(list_N) - 1):
    list_dis.append(list_N[j + 1] - list_N[j])

list_dis.sort()
r = list_dis[0]
for k in range(len(list_dis)):
    r = gcd(r, list_dis[k])

count = 0
for p in range(len(list_dis)):
    count += list_dis[p] // r - 1

print(int(count))