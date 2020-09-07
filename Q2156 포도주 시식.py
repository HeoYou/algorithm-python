n = int(input())

l,dp = [0] * n, [0] * n

for i in range(n):
    l[i] = int(input())

dp[0] = l[0]
if n > 1:
    dp[1] = max(l[1], l[0] + l[1])
if n > 2:
    dp[2] = max(l[2] + l[0], l[2] + l[1])

for i in range(3, n):
    dp[i] = max(l[i] + l[i - 1] + dp[i - 3], l[i] + dp[i - 2])

print(max(dp[-2:]))