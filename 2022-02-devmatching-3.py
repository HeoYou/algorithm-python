dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def make_sea(r, c, l):
    global m, visit
    
    s = [[r, c]]
    
    while s:
        x, y = s.pop()
        visit[x][y] = True
        m[x][y] = l
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if row > nx >= 0 and col > ny >= 0:
                if not visit[nx][ny] and m[nx][ny] == 0:
                    s.append([nx, ny])
                    
def count_lake(r, c):
    global m, visit
    
    s = [[r, c]]
    count = 0
    
    while s:
        x, y = s.pop()
        visit[x][y] = True
        count += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if not visit[nx][ny] and m[nx][ny] == 0:
                s.append([nx, ny])
        
    return count

m = []
visit = []
row, col = 0, 0
lake = []
def solution(rows, columns, lands):
    global m, visit, row, col, lake
    
    row, col = rows, columns
    m = [[0] * columns for i in range(rows)]
    visit = [[False] * (columns) for i in range(rows)]
    
    for x, y in lands:
        m[x - 1][y - 1] = 1
        visit[x - 1][y - 1] = True
        
    make_sea(0, 0, 2)
    
    for i in range(rows):
        for j in range(columns):
            if not visit[i][j] and m[i][j] == 0:
                lake.append(count_lake(i, j))

    return [min(lake), max(lake)] if lake else [-1, -1]

print(solution(5, 6, [[2, 2], [2, 4], [3, 2], [3, 5], [4, 3], [4, 4]]))