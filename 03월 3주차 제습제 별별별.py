import copy

n = int(input())

data = [list(map(int, input().strip().split())) for i in range(n)]
ckData = copy.deepcopy(data)

count = 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dehumi(x, y):
    global data, ckData
    for i in range(4):
        ii, jj = x + dx[i], y + dy[i]
        if ii >= 0 and ii <= n - 1 and jj >= 0 and jj <= n - 1:
            ckData[ii][jj] = 0


def ck(x):
    global ckData
    check = True
    for lst in ckData:
        if i in lst:
            check = False
            return check
    return check


while True:
    if ck(0):
        print(-1)
        break
    if ck(1):
        print(-1)
        break

    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                dehumi(i, j)

    count += 1

    if ck(1) == True:
        print(count)
        break
    data = copy.deepcopy(ckData)