import sys

N, M = map(int, input().split())
dataLst = [0] * N
minArr, maxArr = [0] * M, [0] * M

def minMax(arr):
    minNum, maxNum = 1000000000, 1

    for i in range(len(arr)):
        minNum = minNum if arr[i] > minNum else arr[i]
        maxNum = maxNum if arr[i] < maxNum else arr[i]
    return minNum, maxNum


for i in range(N):
    dataLst[i] = int(sys.stdin.readline())

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    minNum, maxNum = minMax(dataLst[a - 1:b])
    minArr[i] = minNum
    maxArr[i] = maxNum
    

for i in range(M):
    print(minArr[i], end=" ")
    print(maxArr[i])
