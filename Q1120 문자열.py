a, b = map(str, input().split())
minAnswer = 100
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[j + i]:
            count += 1

    minAnswer = min(count, minAnswer)

print(minAnswer)
        
