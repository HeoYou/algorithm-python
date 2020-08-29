N, M = map(int, input().split(' '))
A, B = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
mergeName=""
shtName = min(N, M)
for i in range(shtName):
    mergeName += A[i] + B[i]
mergeName += A[shtName:] + B[shtName:]

arr = []
for i in range(len(mergeName)):
    arr.append(alp[ord(mergeName[i]) - 65])

result = [0 for i in range(N + M)]
for i in range(N + M - 2):
    for j in range(N + M - i - 1):
        arr[j] = (arr[j] + arr[j + 1]) % 10

if arr[0] == 0:
    print(arr[1], end="")
    print("%")
else:
    print(arr[0], end="")
    print(arr[1], end="")
    print("%")







