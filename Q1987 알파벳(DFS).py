import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

r, c = map(int, input().split(' '))
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
lst = []
answer = 0
def dfs(x, y, visit):
    global answer
    visit.append(lst[x][y])
    answer = max(answer, len(visit))

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 <= xx < r and 0 <= yy < c and lst[xx][yy] not in visit:
            dfs(xx, yy, visit)

for i in range(r):
    lst.append(list(input()))

dfs(0, 0, [])


print(answer)