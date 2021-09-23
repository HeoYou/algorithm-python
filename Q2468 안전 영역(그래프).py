dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def dfs(sx, sy, h):
    global visit
    stack = [[sx, sy]]

    while stack:
        x, y = stack.pop()
        visit[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if lst[nx][ny] > h and visit[nx][ny] == 0:
                    stack.append([nx, ny])

for hieght in range(100):
    count = 0
    visit = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if visit[x][y] == 0 and lst[x][y] > hieght:
                count += 1
                dfs(x, y, hieght)

    answer = max(answer, count)

print(answer)


