import sys
import heapq
input = sys.stdin.readline

n, e, x = map(int, input().split())

graph = {}
d = [[10000000] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    graph[i] = []
for e in range(e):
    f, s, v = map(int, input().split())
    graph[f].append([s, v])


for i in range(1, n + 1):

    queue = []
    heapq.heappush(queue, (0, i))

    while queue:

        v, node = heapq.heappop(queue)
        # ---------------------------
        # 이거 두 줄 차이로 3분의 1 줄어듬 속도.
        if d[i][node] < v:
            continue
        # ----------------------------
        for nn, nv in graph[node]:
            nv = nv + v
            if nv < d[i][nn]  and nn != i:
                d[i][nn] = nv
                heapq.heappush(queue, (nv, nn))

answer = 0
for i in range(1, n + 1):
    if i != x:
        answer = max(answer, d[i][x] + d[x][i])
print(answer)
                