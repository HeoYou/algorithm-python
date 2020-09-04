data = [list(map(int, input().split())) for _ in range(10)]
x, y = 1, 1

while True:
    if data[x][y] == 2 or (data[x + 1][y] == 1 and data[x][y + 1] == 1):
        data[x][y] = 9
        break

    data[x][y] = 9
    
    if data[x][y + 1] == 0 or data[x][y + 1] == 2:
        y += 1
    elif data[x + 1][y] == 0 or data[x + 1][y] == 2:
        x += 1


for i in range(10):
    for j in range(10):
        print(data[i][j], end=" ")
    print()

