import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

city = []
root = []

for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))
root = list(map(int, sys.stdin.readline().split()))

flag = True

for i in range(m - 1):
    if root[i] == root[i + 1]:
        continue
    if city[root[i] - 1][root[i + 1] - 1] == 0:
        falg = False
        break
if flag:
    print("YES")
else:
    print("NO")
