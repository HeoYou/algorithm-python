n, m = map(int, input().split(' '))
x, y, d = map(int, input().split(' '))
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

lst = [list(map(int, input().split(' '))) for _ in range(n)]
answer = 0
count = 0
while True:
    if lst[x][y] == 0:
        answer += 1

    lst[x][y] = 2
    
    if lst[dx[d]][dy[d]] == 0:
        d = (d - 1) % 4
        x, y = dx[d], dy[d]
        count = 0
    elif lst[dx[d]][dy[d]] > 0:
        if count == 4 and lst[dx[(d + 2) % 4]][dy[(d + 2) % 4]] == 1:
            break
        else:
            x, y = dx[(d + 2) % 4], dy[(d + 2) % 4]
            
        d = (d - 1) % 4
        count += 1
    
print(lst)
print(answer)
