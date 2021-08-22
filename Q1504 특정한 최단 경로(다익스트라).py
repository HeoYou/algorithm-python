import sys

input = sys.stdin.readline
graph = {}

n, e = map(int, input().split())

for i in range(1, n + 1):
    graph[i] = []

for i in range(e):
    s, e, v = map(int, input().split())
    graph[s].append([e, v])
    graph[e].append([s, v])

v1, v2 = map(int, input().split())


import heapq
def dijkstra(start):
    d = [9876543210] * (n + 1)
    d[start] = 0
    heap = [(0, start)]

    while heap:
        v, node = heapq.heappop(heap)
        if d[node] < v:
            continue
        for nn, nv in graph[node]:
            if nv + v < d[nn]:
                d[nn] = nv + v
                heapq.heappush(heap, (d[nn], nn))
    return d[1:]

nlst = dijkstra(1)
v1lst = dijkstra(v1)
v2lst = dijkstra(v2)



answer = min(nlst[v1 - 1] + v1lst[v2 - 1] + v2lst[n - 1], (nlst[v2 - 1] + v2lst[v1 - 1] + v1lst[n - 1] ))
print(answer if answer < 9000000000 else -1)