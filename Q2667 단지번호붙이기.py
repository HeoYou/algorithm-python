import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    global visit
    global count

    count += 1

    visit[x][y] = 0

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx >= 0 and xx < n and yy >= 0 and yy < n and board[xx][yy] == 1 and visit[xx][yy]:
            dfs(xx, yy)



n = int(input())
visit = [[1 for _ in range(n)] for _ in range(n)]

board = []
answer = []
dx, dy = [0 , 1, 0, -1], [1, 0, -1, 0]
count = 0
for i in range(n):
    board.append(list(map(int, input())))


for i in range(n):
    for j in range(n):
        if visit[i][j] and board[i][j]:
            dfs(i, j)
            answer.append(count)
            count = 0

print(len(answer))
for i in sorted(answer):
    print(i)
