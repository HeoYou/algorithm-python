n = int(input())
line = [0] * n
lst = list(map(int, input().split()))

for i in range(n):
    pos = lst[i]
    count = 0
    for j in range(pos):
        if line[j] != 0:
            count += 1

    

print(' '.join(map(str, line)))
