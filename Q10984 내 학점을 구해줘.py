t = int(input())

for i in range(t):
    sumC, sumG = 0, 0.0
    n = int(input())

    for i in range(n):
        a, b = map(float, input().split(" "))
        sumC += a
        sumG += a * b
    print(int(sumC), round(sumG / sumC, 1))