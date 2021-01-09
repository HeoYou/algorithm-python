import copy
M, N = map(int, input().split())
data = []
answer = 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(N):
    data.append(list(map(int, input().split())))
tmpData = copy.deepcopy(data)


def tomato(x, y):
    global data

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]

        if xx < 0 or xx >= N or yy < 0 or yy >= M:
            continue
        if tmpData[xx][yy] == 0:
            print(123, x, y)
            data[xx][yy] = 1




while True:
    answer += 1
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                print(i, j)
                tomato(i, j)
    
    print(*data, sep='\n')

    if data[:] == tmpData[:]:
        for i in data:
            if 0 in i:
                print(-1)
                exit()
            else:
                print(answer)
                exit()

    tmpData = copy.deepcopy(data)


            


print(data)