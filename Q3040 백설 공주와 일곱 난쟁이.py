data = []

for i in range(9):
    data.append(int(input()))

goalNum = sum(data) - 100
flag = True
for i in range(8):
    for j in range(i + 1, 9):
        if flag == False:
            break
        if data[i] + data[j] == goalNum:
            flag = False
            data.pop(j)
            data.pop(i)
            break

print("\n".join(map(str, data)))

