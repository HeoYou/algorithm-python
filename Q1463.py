n = int(input())

dp = [0 for i in range(1000001)]

while n > 1:

    if dp[n - 1] > dp[n] + 1 or dp[n - 1] == 0:
        dp[n - 1] = dp[n] + 1
    if n % 2 == 0 and (dp[n // 2] > dp[n] + 1 or dp[n // 2] == 0):
        dp[n // 2] = dp[n] + 1
    if n % 3 == 0 and (dp[n // 3] > dp[n] + 1 or dp[n // 3] == 0):
        dp[n // 3] = dp[n] + 1
    n -= 1;

print(dp[1])
