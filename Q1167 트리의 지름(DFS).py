
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = {}
# visit = [[0, 0] for i in range(n + 1)]
visit = [0] * (n + 1)

for i in range(n):
    tree = list(map(int, input().split(' ')))
    if graph.get(tree[0], None) == None:
        graph[tree[0]] = []
    for c in range(1, len(tree) - 1, 2):
        graph[tree[0]].append([tree[c], tree[c + 1]])

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

        



