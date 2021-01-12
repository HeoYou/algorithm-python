N, L = map(int, input().split())

answer = 0
pos = 0
lst = sorted(list(map(int, input().split())))
lst.append(10000)

for i in range(len(lst)):
    if lst[i] - lst[pos] >= L:
        answer += 1
        pos = i

print(answer)