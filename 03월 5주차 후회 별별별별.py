import sys

n, m = map(int, sys.stdin.readline().split(" "))

a = list(map(int, sys.stdin.readline().strip().split(" ")))

for i in range(m):
    sumLst = 0
    data = list(map(int, sys.stdin.readline().strip().split(" ")))    

    if data[0] == 1:
        # print(sum(a[data[1] - 1:data[2]]))
        for i in range(data[1], data[2] + 1):
            sumLst += a[i - 1]
        print(sumLst)

    else:
        a[data[1]-1] -= data[2]

        