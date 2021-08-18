n, k = map(int, input().split())

lst = [0] * 1001

lst[0] = 1

for i in range(1, n + 1):
    lst[i] = lst[i - 1] * i

print((lst[n] // (lst[k] * lst[n - k])) % 10007)


