
n = int(input())
answer = 0

lstA = list(map(int, input().split())) + [0]
lstB = list(map(int, input().split())) + [0]

dpA = [0] * (n + 2)
dpA[0] = lstA[0]

dpB = [0] * (n + 2)
dpB[0] = lstB[0]

for i in range(n):
    dpA[i + 1] = dpA[i] + lstA[i + 1]
    dpB[i + 1] = dpB[i] + lstB[i + 1]
    
    for j in range(i + 1):
        # print(i, j)
        
        if i == j:
            if lstA[i] == lstB[i]:
                answer += 1
                # print("=", i, j)
        elif dpA[i] - dpA[j - 1] == dpB[i] - dpB[j - 1]:
            # print(dpA[i], dpA[j - 1], dpB[i], dpB[j - 1])
            answer += 1
#     print()
# print(dpA)
# print(dpB)
print(answer)