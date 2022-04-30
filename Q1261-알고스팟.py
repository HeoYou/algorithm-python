import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

M, N = map(int, input().split())

graph = [list(map(int, list(input().strip()))) for i in range(N)]
visit1 = [[INF] * M for i in range(N)]
visit1[0][0] = 0
q = deque([(0, 0)])

while q:
    data = q.popleft()
    x, y = data[0], data[1]
 
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 > nx or nx >= N or 0 > ny or ny >= M:
            continue
        if visit1[x][y] + graph[nx][ny] < visit1[nx][ny]:
            visit1[nx][ny] = visit1[x][y] + graph[nx][ny]
            q.append((nx, ny))
   
print(visit1[N - 1][M - 1])