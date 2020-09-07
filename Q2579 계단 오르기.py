import sys
n = int(input())
l = [0] * n
dp = [0] * n
for i in range(n):
    l[i] = int(sys.stdin.readline()) 

dp[0] = l[0]
if n > 1:
    dp[1] = max(l[0] + l[1], l[1])
if n > 2:
    dp[2] = max(l[0] + l[2], l[1] + l[2])

for i in range(3, n):
    dp[i] = max(dp[i -2] + l[i],dp[i - 3] + l[i - 1] + l[i])

print(dp[n - 1])
