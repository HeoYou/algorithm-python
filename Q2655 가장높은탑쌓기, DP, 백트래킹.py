n = int(input())
brick = [[0] * 4]

for i in range(1, n + 1):
    brick.append([i] + list(map(int, input().split())))
brick = sorted(brick, key = lambda x:x[3])
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if brick[i][1] > brick[j][1]:
            dp[i] = max(dp[i], dp[j] + brick[i][2])
max_value = max(dp)
index = n
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(brick[index][0])
        max_value -= brick[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]

