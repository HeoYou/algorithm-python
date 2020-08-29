import sys

t = int(input())

for i in range(t):
    n = int(sys.stdin.readline())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        a, b = 0, 1

        for j in range(n - 1):
            a, b = b, a + b
        print(a, b)





