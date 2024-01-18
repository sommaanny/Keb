import sys
from collections import deque

# N = int(sys.stdin.readline())  #백준 18258
# list_que = deque()
# for i in range(N):
#     command = sys.stdin.readline().rstrip().split()
#     if len(command) == 2:
#         list_que.append(int(command[1]))
#     else:
#         if command[0] == 'pop':
#             if len(list_que) != 0:
#                 print(list_que.popleft())
#             else:
#                 print(-1)
#         elif command[0] == 'size':
#             print(len(list_que))
#         elif command[0] == 'empty':
#             if len(list_que) == 0:
#                 print(1)
#             else:
#                 print(0)
#         elif command[0] == 'front':
#             if len(list_que) != 0:
#                 print(list_que[0])
#             else:
#                 print(-1)
#         elif command[0] == 'back':
#             if len(list_que) != 0:
#                 print(list_que[-1])
#             else:
#                 print(-1)

# N = int(sys.stdin.readline())   #백준 2164
# list_card = deque([i for i in range(1, N + 1)])
# while(len(list_card) > 1):
#     list_card.popleft()
#     list_card.append(list_card.popleft())
# print(list_card[0])

# N, K = map(int, sys.stdin.readline().split()) #백준 28279
# list_people = deque([i for i in range(1, N + 1)])
# print("<",end='')
# while(len(list_people) != 0):
#     for j in range(K - 1):
#         list_people.append(list_people.popleft())
#     if len(list_people) > 1:
#         print(list_people.popleft(), end=', ')
#     else:
#         print((list_people.popleft()),end='>')
