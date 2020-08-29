sum = 0
minNum = 100
for _ in range(7):
    data = int(input())
    if data % 2 == 1: 
        sum = sum + data
        minNum = min(data, minNum)

if sum != 0:
    print(sum)
    print(minNum)
else:
    print(-1)