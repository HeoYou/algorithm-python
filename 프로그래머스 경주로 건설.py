# 우선 시간초과 같은 경우는 지금 함수형 문제로 만들면 안될거같다
# 나중에 while형태로 수정 하는게 시간초과 해결방법 테케는 통과하는데 어디서 문제인지 모르겠다.


# 1. 상 2. 우 3. 하 4. 좌
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
global_map = []
board = []
size = 0
def solution(b):
    global global_map, board, size
    board = b
    answer = 100000
    size = len(b)
    global_map = [[100000 for i in range(size)] for _ in range(size)]
    bfs(0, 0, 1, 0)
    answer = min(global_map[-1][-1], answer)
    global_map = [[100000 for i in range(size)] for _ in range(size)]
    bfs(0, 0, 2, 0) 
    answer = min(global_map[-1][-1], answer)
    
    return answer

def bfs(x, y, d, m):
    global global_map
    global_map[x][y] = m
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 > nx or size <= nx or 0 > ny or size <= ny:
            continue
        if board[nx][ny] == 0 and global_map[nx][ny] > m:
            if i == d:
                bfs(nx, ny, i, m + 100)
            else:
                bfs(nx, ny, i, m + 600)

print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))