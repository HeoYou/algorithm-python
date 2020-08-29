import sys

t = int(input())
lst = [1, 1, 1, 2, 2]
for i in range(5, 101):
    lst.append(lst[i - 3] + lst[i - 2])
for _ in range(t):
    n = int(sys.stdin.readline())
    print(lst[n -1])