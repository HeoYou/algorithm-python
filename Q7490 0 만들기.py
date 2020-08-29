import sys
sys.setrecursionlimit(10**6)

def toZero(n, N, arr):
    if n == N:
        if eval(arr.replace(" ", "")) == 0:
            print(arr)
            return
        else:
            return
    toZero(n + 1, N, arr + " " + str(n + 1))
    toZero(n + 1, N, arr + "+" + str(n + 1))
    toZero(n + 1, N, arr + "-" + str(n + 1))
    
for _ in range(int(input())):
    n = int(input())
    toZero(1, n, "1")
    print()

