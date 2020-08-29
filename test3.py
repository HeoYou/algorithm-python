N, K = map(int, input().split(" "))

data = list(map(int, input().split(" ")))
arr = []

for i in range(K - 1):
    arr.append(data[i:i + 1])
arr.append(data[K - 1:])
costArr = [0 for i in range(K)]

if K == 1:
    print(max(data) - min(data))
else:

    for i in range(K - 1, 0, -1):
        for j in range(N - K):
            arr[i - 1].append(arr[i].pop(0))
            for x in range(K):
                if len(arr[x]) == 1:
                    costArr[x] = 0
                else:
                    costArr[x] = max(arr[x]) - min(arr[x])

    print(max(costArr))

