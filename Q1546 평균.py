n = int(input())
data = []

data = list(map(int, input().split(' ')))

max = max(data)
sum = 0

for i in data:
    sum += i
sum = sum / n

print((sum / max) * 100)
