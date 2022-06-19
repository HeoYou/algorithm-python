import pprint
import sys

from collections import deque

input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

N, M = map(int, input().split())
board = [list(input()) for i in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
q = deque()
rx, ry, bx, by =  0, 0, 0, 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
            
q.append((rx, ry, bx, by, 1))
visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    count = 0
    
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
        
    return x, y, count

def bfs():
    
    while q:
        rx, ry, bx, by, depth = q.popleft()
        
        if depth > 10:
            break
        
        for i in range(4):
            nrx, nry, r_count = move(rx, ry, dx[i], dy[i])
            nbx, nby, b_count = move(bx, by, dx[i], dy[i])
            
            if board[nbx][nby] != 'O':
                if nrx == nbx and nry == nby:
                    return depth + 1

                if nrx == nbx and nry == nby:
                    if r_count > b_count:
                        nrx, nry = nrx-dx, nry-dy
                    else:
                        nbx, nby = nbx-dx, nby-dy

                if (nrx,nry,nbx,nby) in visited:
                    continue
                else:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, depth + 1))
                    # print("방문처리 : ", nrx, nry, nbx, nby, cnt+1)

    return -1
        
print(N, M)
pprint.pprint(board)
print(bfs())