import sys

N, M = map(int, input().split())
dataLst = []
minArr, maxArr = [], []
for i in range(N):
    dataLst.append(int(sys.stdin.readline()))

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    minArr.append(min(dataLst[a - 1:b]))
    maxArr.append(max(dataLst[a - 1:b]))

for i in range(M):
    print(minArr[i], end=" ")
    print(maxArr[i])