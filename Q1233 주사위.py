s1, s2, s3 = map(int, input().split())
lst = [0] * (s1 + s2 + s3 + 1)

for i in range(s1):
    for j in range(s2):
        for k in range(s3):
            sum = (i + 1) + (j + 1) + (k + 1)
            lst[sum] += 1
print(lst.index(max(lst)))