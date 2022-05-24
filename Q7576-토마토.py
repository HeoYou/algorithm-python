from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
data = []
answer = -1
q = deque([])
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(N):
    data.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            q.append([i, j])


def tomato():
    global data, q
    
    while q:
        
        x, y = q.popleft()
        
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
    
            if xx < 0 or xx >= N or yy < 0 or yy >= M or data[xx][yy] == -1:
                continue
            if data[xx][yy] == 0:
                data[xx][yy] = data[x][y] + 1
                q.append([xx, yy])

tomato()
for i in data:
	for j in i:
		if j == 0:
			print(-1)
			exit(0)
		answer = max(answer, j)
print(answer - 1)