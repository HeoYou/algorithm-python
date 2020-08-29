n = int(input())
data = [list(map(int, input().strip().split())) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
maxLen = 0

def dfs(x, y, lengh):
    global maxLen
    maxLen = max(lengh, maxLen)

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]

        if xx >= 0 and xx < n and yy >= 0 and yy < n:
            if data[x][y] > data[xx][yy]:
                dfs(xx, yy, lengh + 1)

for i in range(n):
    for j in range(n):
        dfs(i, j, 1)

print(maxLen)