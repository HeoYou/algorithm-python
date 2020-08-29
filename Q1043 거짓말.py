N, M = map(int, input().split())
data = list(map(int, input().split()))

know = [0] * (N + 1)
count = 0
for i in data:
    know[i] = 1

for i in range(M):
    mem = list(map(int, input().split()))
    flag = True
    for j in mem:
        if know[j] == 1:
            flag = False
            for k in mem:
                know[k] = 1
            break
    if flag:
        count += 1

    
print(count)