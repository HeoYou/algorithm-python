from collections import deque

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
result = []
indegree = [0] * (n + 1)
q = deque()

for i in range(m):
    a, b = map(int, input().split())
    
    indegree[b] += 1
    graph[a].append(b)

for i in range(1, n):
    if indegree[i] == 0:
        q.append(i)
    
while q:
    node = q.popleft()
    result.append(node)
    for i in graph[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
        
print(result, q, graph, indegree)

