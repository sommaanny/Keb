import sys

# N = int(sys.stdin.readline()) #백준 9012

# for i in range(N):
#     stack_x = list()
#     p = sys.stdin.readline().rstrip()
#     for i in p:
#         if i == '(':
#             stack_x.append(i)
#         else:
#             if stack_x:
#                 stack_x.pop()
#             else:
#                 print("NO")
#                 break
#     else:
#         if stack_x:
#             print("NO")
#         else:
#             print("YES")

# while(True):   #백준 4949
#     _string = sys.stdin.readline().rstrip()
#     if _string == '.':
#         break
#     else:
#         stack = list()
#         for i in _string:
#             if i == '(' or i == '[':
#                 stack.append(i)
#             elif i == ')':
#                 if stack and stack[-1] == '(':
#                     stack.pop()
#                 else:
#                     print("no")
#                     break
#             elif i == ']':
#                 if stack and stack[-1] == '[':
#                     stack.pop()
#                 else:
#                     print("no")
#                     break
#         else:
#             if stack:
#                 print("no")
#             else:
#                 print("yes")

# N = int(sys.stdin.readline())   # 백준 12789
# list_std = list(map(int, sys.stdin.readline().split()))
# stack_space = []
# count = 1
# while(True):
#     if len(list_std) != 0:
#         if list_std[0] == count:
#             del list_std[0]
#             count += 1
#         elif len(stack_space) != 0 and stack_space[-1] == count:
#             stack_space.pop()
#             count += 1
#         else:
#             stack_space.append(list_std[0])
#             del list_std[0]
#     else:
#         if len(stack_space) == 0:
#             print("Nice")
#             break
#         else:
#             if stack_space[-1] == count:
#                 stack_space.pop()
#                 count += 1
#             else:
#                 print("Sad")
#                 break
