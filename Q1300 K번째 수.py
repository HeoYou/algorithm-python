n, k = map(int, input().split())

lst = [i * j for j in range(1, n + 1) for i in range(1, n + 1)]

print(sorted(lst))