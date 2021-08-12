n, m = map(int, input().split(' '))
x, y, d = map(int, input().split(' '))
lst = [list(map(int, input().split(' '))) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

answer = 0

while True:
# for i in range(100):
    print(x, y, d)
    
    flag = 0
    if lst[x][y] == 0:
        lst[x][y] = 2
        answer += 1
    for i in lst:
        print(i)
    # d = (d - 1) % 4
    # if lst[dx[d]][dy[d]] == 0:
    #     print(123123)
    #     x, y = x + dx[d], y + dy[d]
    #     continue
    for i in range(4):
        d = (d - 1) % 4
        print('d', d, i)
        xx, yy = x + dx[d], y + dy[d]
        print('np', xx, yy)
        if lst[xx][yy] == 0:
            flag = 1
            break
    if flag:
        x, y = xx, yy
    else:
        if lst[(d - 2) % 4][(d - 2) % 4] != 1:
            x, y = x + dx[(d - 2) % 4], y + dy[(d - 2) % 4]
        else:
            print('break')
            break

    
print(answer)

for i in lst:
    print(i)
