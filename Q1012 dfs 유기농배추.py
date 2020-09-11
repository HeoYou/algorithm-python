# import sys
# sys.setrecursionlimit(10000)

# t = int(input())

# b, ck = [], []

# dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

# def dfs(x, y):
#     global b, ck
#     if ck[x][y] == 1:
#         return
#     ck[x][y] = 1
#     for i in range(4):
#         xx, yy = x + dx[i], y + dy[i]
#         if b[xx][yy] == 0 or ck[xx][yy] == 1:
#             continue
#         dfs(xx, yy)

# def process():
#     global b, ck

#     m, n, k = map(int, input().split())
    
#     b = [[0 for i in range(m + 2)] for _ in range(n + 2)]
#     ck = [[0 for i in range(m + 2)] for _ in range(n + 2)]


#     for _ in range(k):
#         x, y = map(int, input().split())
#         b[y+1][x+1] = 1

#     ans = 0
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if b[i][j] == 0 or ck[i][j] == 1:
#                 continue
#             dfs(i, j) 
#             ans += 1
#     print(ans)



# for _ in range(t):
#     process()
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global ckField, field, dx, dy
    ckField[x][y] = 1

    for i in range(4):
        xx, yy = dx[i] + x, dy[i] + y
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if field[xx][yy] == 1 and ckField[xx][yy] == 0:
            dfs(xx, yy)
                


tc = int(input())
field, ckField = [], []
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(tc):

    count = 0
    m , n, k = map(int, input().split())
    field = [[0] * m for i in range(n)]
    ckField = [[0] * m for i in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and ckField[i][j] == 0:
                dfs(i, j)
                count += 1
    print(count)


