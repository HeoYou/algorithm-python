n, s, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True

for i in range(n):
    for j in range(m + 1):
        if dp[i][j] == True:
            # print(j, arr[i])
            # for x in range(len(dp)):
            #     print(dp[x])
            if j + arr[i] <= m:
                dp[i + 1][j + arr[i]] = True
            if j - arr[i] >= 0:
                dp[i + 1][j - arr[i]] = True
answer = -1
for i in range(m, -1, -1):
    if dp[-1][i] == True:
        answer = i
        break

print(answer)
            
