n, k = map(int, input().split())

lst = list(map(int, input().strip().split()))

ans = 0

for i in range(0, n - 1):
    for j in range(i, n):
        ans = max(ans, (k // lst[i] * lst[j]) + k % lst[i])

print(ans)
