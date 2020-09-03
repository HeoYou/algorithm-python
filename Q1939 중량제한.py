import sys
from collections import deque

N, M = map(int, input().split())
data = [[] for _ in range(N + 1)]

def bfs(c):
    queue = deque([start_node])
    visited = [False] * (N + 1)
    visited[start_node] = True
    
    while queue:
        x = queue.popleft()

        for y, weight in data[x]:

            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)

    return visited[end_node]

start = 1000000000
end = 1

for i in range(M):
    x, y, w = map(int, sys.stdin.readline().split())
    data[x].append((y, w))
    data[y].append((x, w))
    start = min(start, w)
    end = max(end, w)

start_node, end_node = map(int, sys.stdin.readline().split())


answer = start
while(start <= end):
    mid = (start + end) // 2
    if bfs(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)