import sys
t = int(input())

for _ in range(t):
    n = int(input())
    data = []
    count = 1   
    for i in range(n):
        data.append(list(map(int, sys.stdin.readline().split())))

    data = sorted(data)
    maxData = data[0][1]

    for i in range(n):
        if maxData == n + 1:
            break
        else:
            if maxData > data[i][1]:
                maxData = data[i][1]
                count += 1
        
    print(count)