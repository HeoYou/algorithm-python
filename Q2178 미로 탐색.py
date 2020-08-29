import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
data = []
answer = []
visit = [[0 for i in range(M)] for j in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(N):
    data.append(list(map(int, list(input()))))

def dfs(x, y, count, v):
    global answer

    v[x][y] = 1
    if x == N - 1 and y == M - 1:
        answer.append(count)
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx >= 0 and xx < N and yy >= 0 and yy < M:
            if data[xx][yy] == 1 and v[xx][yy] == 0:
                print(count)
                print(v)
                count += 1
                dfs(xx, yy, count, v)

dfs(0, 0, 1, visit)
print(answer)
