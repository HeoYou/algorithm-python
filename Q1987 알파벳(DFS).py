# import sys
# limit_number = 15000
# sys.setrecursionlimit(limit_number)

# r, c = map(int, input().split(' '))
# dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
# lst = []
# answer = 0
# def dfs(x, y, visit):
#     global answer
#     visit.append(lst[x][y])
#     answer = max(answer, len(visit))

#     for i in range(4):
#         xx, yy = x + dx[i], y + dy[i]
#         if 0 <= xx < r and 0 <= yy < c and lst[xx][yy] not in visit:
#             dfs(xx, yy, visit)
# for i in range(r):
#     lst.append(list(input()))

# dfs(0, 0, [])


# print(answer)


import sys
import copy
sys.setrecursionlimit(10000)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int, input().split())
lst = [list(input()) for i in range(n)]
count_lst = [[0] * m for i in range(n)]

def dfs(x, y, c, visit):
    global count_lst
    count_lst[x][y] = c
    visit = copy.deepcopy(visit) 
    visit[lst[x][y]] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visit[lst[nx][ny]] == 0 and count_lst[nx][ny] <= c:
                dfs(nx, ny, c + 1, visit)
    for i in count_lst:
        print(i)
    print()

dic = {chr(i):0 for i in range(65, 91)}
dfs(0, 0, 1, dic)
print(count_lst)
