import sys
input = sys.stdin.readline
n = int(input())
lst = [0] * n
for i in range(n):
    lst[i] = list(map(int, input().split()))

lst = sorted(sorted(lst), key = lambda x : x[1])
for i, j in lst:
    print(i, j)