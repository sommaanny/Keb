import sys

N = int(sys.stdin.readline())
M = list(map(int,sys.stdin.readline().split()))

if N == 1:
    print(M[0] * M[0])
else:
    M.sort()
    print(M[0] * M[-1])