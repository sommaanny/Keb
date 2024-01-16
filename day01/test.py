import sys

N = int(sys.stdin.readline())
stack_x = list()

for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n != 0:
        stack_x.append(n)
    else:
        stack_x.pop()

print(sum(stack_x))