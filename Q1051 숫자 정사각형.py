r, c = map(int, input().split())
lst = [list(input()) for i in range(r)]

answer = 1
next = 0
for i in range(r - 1):
    for j in range(c - 1):
        next = 1
        while i + next < r and j + next < c:
            if lst[i][j] == lst[i][j + next] == lst[i + next][j] == lst[i + next][j + next]:
                answer = max(answer, (next + 1) ** 2)
            next += 1

print(answer)
