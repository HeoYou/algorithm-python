n = int(input())

a, b = 1, 2

for i in range(n - 2):
    a, b = b, a + b

print(b % 10007 if n > 1 else a)


