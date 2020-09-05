N = int(input())
sumN = 0
for i in range(N):
    if N == sum([int(j) for j in str(i)]) + i:
        sumN = i
        break
print(sumN)