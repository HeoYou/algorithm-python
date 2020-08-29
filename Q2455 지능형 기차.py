max1, max2 = 0, 0

for i in range(4):
    a, b = map(int, input().split())
    max2 -= a
    max2 += b
    max1 = max(max1, max2)

print(max1)
