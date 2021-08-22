from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(0)
    exit()

graph = {}
# visit = [[0, 0] for i in range(n + 1)]
visit = [0] * (n + 1)
for i in range(n):
    graph[i + 1] = []
for i in range(n - 1):
    f, s, v = map(int, input().split())
    graph[f].append([s, v])
    graph[s].append([f, v])

queue = deque()
queue.append([1, 0])
max_n, max_v = 0, 0
while queue:
    node, v = queue.popleft()
    visit[node] = 1

    for nn, nv in graph[node]:
        if visit[nn] == 0:
            nv = v + nv
            queue.append([nn, nv])
            if nv > max_v:
                max_n = nn
                max_v = nv

visit = [0] * (n + 1)
queue.append([max_n, 0])
max_n = 0
while queue:
    node, v = queue.popleft()
    visit[node] = 1

    for nn, nv in graph[node]:
        if visit[nn] == 0:
            nv = v + nv
            queue.append([nn, nv])
            if nv >= max_v:
                max_n = nn
                max_v = nv
print(max_v)

        



