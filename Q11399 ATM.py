n = int(input())
sum = 0

data = list(map(int, input().split()))
data.sort()

for i in range(n):
    sum += data[i] * (n - i)

print(sum)
