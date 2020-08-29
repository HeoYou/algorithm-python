import sys

sys.setrecursionlimit(10 ** 7)

dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]


# def dfs(x, y):
#     global ck
#     ck[x][y] = 1
#     for i in range(8):
#         xx, yy = x + dx[i], y + dy[i]
#         if xx >= 0 and xx < w and yy >= 0 and yy < h:
#             if lst[yy][xx] == 1 and ck[yy][xx] == 0:
#                 dfs(yy, xx)
#                 pass
    

# while True:
#     lst, ck= [], []
#     count = 0
#     w, h = map(int, input().strip().split())
#     if w == 0 and h == 0:
#         break

#     for _ in range(h):
#         lst.append(list(map(int, input().strip().split())))
#         ck.append([0] * w)

#     for i in range(h):
#         for j in range(w):
#             if lst[i][j] == 1 and ck[i][j] == 0:
#                 count += 1
#                 dfs(j, i)

#     print(count)

def dfs(x, y):
    global ck
    ck[x][y] = 1

    for i in range(8):
        xx, yy = x + dx[i], y + dy[i]
        if xx >= 0 and xx < h and yy >= 0 and yy < w:
            if lst[xx][yy] == 1 and ck[xx][yy] == 0:
                dfs(xx, yy)
                


while True:

    lst, ck = [], []
    count = 0
    w, h = map(int, input().strip().split())
    if w == 0 and h == 0:
        break
    for _ in range(h):
        lst.append(list(map(int, input().strip().split())))
        ck.append([0] * w)

    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1 and ck[i][j] == 0:

                count += 1
                dfs(i, j)

    print(count)