n, m = map(int, input().split(" "))

a = list(map(int, input().strip().split(" ")))
b = list(map(int, input().strip().split(" ")))

alst = {i: 0 for i in a}

for i in a:
    alst[i] = alst[i] + 1

ans = [0 for i in range(m)]

for i in range(m):
    if b[i] in alst:
        ans[i] = alst[b[i]]
    else:
        ans[i] = 0

for i in ans:
    print(i, end=" ")
