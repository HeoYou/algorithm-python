import sys
n, m = map(int, input().split())
answer = []
graph = [[] for i in range(n + 1)]
maxCount = 0

def dfs(v):
    stack = [v]
    visit = []

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node]) 
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

