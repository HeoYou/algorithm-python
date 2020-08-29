import sys

sys.setrecursionlimit(10 ** 6)

x, y = map(int, input().split())
data = []
dp = [[-1] * y for i in range(x)]

print(dp)
answer = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(x):
    data.append(list(map(int, input().split())))

def find(a, b, val):
    global answer
    if a == x - 1 and b == y - 1:
        answer += 1
        return
    if a < 0 or a >= x or b < 0 or b >= y:
        return
    if val <= data[a][b]:
        return
    

    for i in range(4):
        find(a + dx[i], b + dy[i], data[a][b])

def find2(a, b):
    global dp
    if a == 0 and b == 0:
        return 1
    if dp[a][b] == -1:
        dp[a][b] = 0
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
        
            if nx >= 0 and nx < x and ny >= 0 and ny < y and data[a][b] < data[nx][ny]:
                dp[a][b] += find2(nx, ny)


print(find2(x - 1, y - 1))
