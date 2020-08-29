n = int(input())

a = list(map(int, input().split(" ")))

p = [i for i in range(n - 1)]

b = [0 for i in range(n)]

for i in range(n - 1):
    b[p[i]] = a[i]

print(''.join(b))
