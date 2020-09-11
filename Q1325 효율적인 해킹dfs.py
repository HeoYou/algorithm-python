import sys
from collections import deque

n, m = map(int, input().split())
answer = []
graph = [[] for i in range(n + 1)]
maxCount = 0

def dfs(v):
    q = deque([v])
    visit = []

    while q:
        node = q.popleft()
        if node not in visit:
            visit.append(node)
            q.extend(graph[node]) 
    return len(visit)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

for i in range(1, n + 1):

    tmp = dfs(i)
    if tmp > maxCount:
        answer = [i]
        maxCount = tmp
    elif tmp == maxCount:
        answer.append(i)

print(' '.join(map(str, answer)))

