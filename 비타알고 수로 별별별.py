n = int(input())
data = []
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for _ in range(n):
    data.append(list(map(int, input().strip().split())))
count = 0

def dfs(x, y):
    global count

    if x == n - 1 and y == n - 1:
        count += 1
    
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]

        if xx >= 0 and xx < n and yy >= 0 and yy < n:
            if data[x][y] > data[xx][yy]:
                dfs(xx, yy)

dfs(0, 0)
print(count)

        

