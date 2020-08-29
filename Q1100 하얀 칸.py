chessLst = list()
count = 0
for i in range(8):
    chessLst.append(list(map(str, input())))

for i in range(8):
    for j in range(8):
        if i % 2:
            if j % 2:
                if chessLst[i][j] == "F":
                    count += 1
                
        else:
            if not j % 2:
                if chessLst[i][j] == "F":
                    count += 1

print(count)
