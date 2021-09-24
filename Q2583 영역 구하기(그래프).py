dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

m, n, area = map(int, input().split())

lst = [[True] * n for _ in range(m)]

for i in range(area):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            lst[x][y] = False
for i in lst:
    print(i)

answer = 0
visit = [[0] * n for _ in range(m)]

def dfs(sx, sy):
    global visit
    stack = [[sx, sy]]
    count = -1

    while stack:
        x, y = stack.pop()
        count += 1
        visit[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if lst[nx][ny] and visit[nx][ny] == 0:
                    stack.append([nx, ny])
    return count

answer = []
for x in range(m):
    for y in range(n):
        if visit[x][y] == 0 and lst[x][y]:
            answer.append(dfs(x, y))

print(len(answer))
print(' '.join(map(str, answer)))



