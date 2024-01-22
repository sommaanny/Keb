import sys
from collections import deque

# N = int(sys.stdin.readline())  #백준 28279
# list_deque = deque()
# for i in range(N):
#     command = list(map(int,sys.stdin.readline().rstrip().split()))
#     if len(command) == 2: # push
#         if command[0] == 1:
#             list_deque.appendleft(command[1])
#         else:
#             list_deque.append(command[1])
#     else:
#         if command[0] == 3:
#             if len(list_deque) != 0:
#                 print(list_deque.popleft())
#             else:
#                 print(-1)
#         elif command[0] == 4:
#             if len(list_deque) != 0:
#                 print(list_deque.pop())
#             else:
#                 print(-1)
#         elif command[0] == 5:
#             print(len(list_deque))
#         elif command[0] == 6:
#             if len(list_deque) != 0:
#                 print(0)
#             else:
#                 print(1)
#         elif command[0] == 7:
#             if len(list_deque) != 0:
#                 print(list_deque[0])
#             else:
#                 print(-1)
#         elif command[0] == 8:
#             if len(list_deque) != 0:
#                 print(list_deque[-1])
#             else:
#                 print(-1)

# N = int(sys.stdin.readline()) #백준 2346
# number = deque((map(int, sys.stdin.readline().split())))
# balloon = deque([i for i in range(1, N + 1)])

# while(len(number) != 0):
#     if number[0] > 0:
#         print(balloon.popleft(), end=' ')
#         for i in range(number.popleft() - 1):
#             if number:
#                 number.append(number.popleft())
#                 balloon.append(balloon.popleft())
#     else:
#         print(balloon.popleft(), end=' ')
#         for i in range(-1 * number.popleft()):
#             if number:
#                 number.appendleft(number.pop())
#                 balloon.appendleft(balloon.pop())

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

count_zero = A.count(0)

# for i in range(M):
#     return_x = C[i]
#     index = 0
#     for j in A:
#         if j == 0: #que 일때
#             tmp = return_x
#             return_x = B[index]
#             B[index] = tmp
#             index += 1
#         else:
#             index += 1
#     print(return_x, end= ' ')


if count_zero == 0:
    for i in C:
        print(i, end=' ')
else: #큐를 이어붙이면 앞으로 들어가고 맨 뒤에게 빠져나와 출력됨
    result = deque([B[i] for i in range(N) if A[i] != 1])
    for j in C:
        result.appendleft(j)
        print(result.pop(), end=' ')
