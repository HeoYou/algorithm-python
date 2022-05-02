# import sys
# from collections import deque

# input = sys.stdin.readline
# INF = int(1e9)

# dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# N, M = map(int, input().split())

# graph = [list(map(int, list(input().strip()))) for i in range(N)]
# visit1 = [[INF] * M for i in range(N)]
# visit1[0][0] = 0
# visit2 = [[1] * M for i in range(N)]
# q = deque([(0, 0)])

# while q:
# 	data = q.popleft()
	
# 	x, y = data[0], data[1]
	
# 	for i in range(4):
# 		nx, ny = x + dx[i], y + dy[i]
# 		if 0 > nx or nx >= N or 0 > ny or ny >= M:
# 			continue
# 		if visit1[x][y] + graph[nx][ny] < visit1[nx][ny]:
# 			visit1[nx][ny] = visit1[x][y] + graph[nx][ny]
# 			visit2[nx][ny] = visit2[x][y] + 1
# 			q.append((nx, ny))
# if visit1[N-1][M-1] >= 2:
# 	print(-1)
# else:
# 	print(visit2[N-1][M-1])
	


from collections import deque

n, m = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))