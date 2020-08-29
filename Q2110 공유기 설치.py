import sys
N, C = map(int, sys.stdin.readline().split())

data = []
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
data.sort()

print(data)