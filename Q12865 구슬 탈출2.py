import time
import timeit
N, M = map(int, input().split())
mapLst = [list(map(str, input())) for _ in range(N)]
if M > N:
    for i in range(N, M):
        mapLst.append(['#' for i in range(M)])
elif N > M:
    for i in range(N):
        for j in range(M, N):
            mapLst[i].append("#")    

def rotate_90(m): 
    N = len(m) 
    ret = [[0] * N for _ in range(N)] 
    for r in range(N): 
        for c in range(N): 
            ret[c][N-1-r] = m[r][c] 
    return ret

def findBall(lst, color):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == color:
                return i, j
x, y = findBall(mapLst, 'B')

def moveBall(lst, count):
    if count > 10:
        return 100

    rx, ry = findBall(lst, "R")
    bx, by = findBall(lst, "B")

    for i in range(max(ry, by) + 1):
        if lst[rx - 1][ry - 1] == '.':
            lst[rx][ry], lst[rx - 1][ry - 1] = lst[rx - 1][ry - 1], lst[rx][ry]
        elif lst[rx - 1][ry - 1] == 'O':
            return count
        
        if lst[bx - 1][by - 1] == '.':
            lst[bx][by], lst[bx - 1][by - 1] = lst[bx - 1][by - 1], lst[bx][by]
        elif lst[bx - 1][by - 1] == 'O':
            return 100

        if lst[rx - 1][ry - 1] == '#' and lst[bx - 1][by - 1] == '#':
            break

    for i in range(4):
        lst = rotate_90(lst)
        minAns = min(100, moveBall(lst, count + 1))
    return minAns

answer = 100
startTime = timeit.default_timer()
for i in range(4):
    mapLst = rotate_90(mapLst)
    answer = min(answer, moveBall(mapLst, 1))
print(startTime - timeit.default_timer())
print(-1 if answer > 10 else answer)