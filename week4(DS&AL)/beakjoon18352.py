import sys
from collections import deque
              
N, M, K, X = map(int, sys.stdin.readline().split())
graph_N = [[] for j in range(N + 1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph_N[x].append(y)

distance = [-1] * (N + 1)
distance[X] = 0
queue = deque([X])

while queue:
    now = queue.popleft()
    for next in graph_N[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)

print(distance)