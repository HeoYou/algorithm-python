import heapq
from collections import deque

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

N = int(input())

board = [[2] + [0] * (N) + [2] for i in range(N)]
board = [[2] * (N + 2)]+ board + [[2] * (N + 2)]
board[1][1] = 2

next_dir = deque()
snake = deque()
snake.append([1, 1])
direction = 1   # 0위 1오 2아래 3왼

for i in range(K := int(input())):
    a, b = map(int, input().split())
    board[b][a] = 1

for i in range(int(input())):
    a, b = input().split()
    next_dir.append([int(a), b])
    
x, y = 1, 1
answer = 0

while True:
    
    answer += 1
    
    x, y = x + dx[direction], y + dy[direction]
    if next_dir and answer == next_dir[0][0]:
        a, D = next_dir.popleft()
        if D == "L":
            direction = (direction - 1) % 4
        if D == "D":
            direction = (direction + 1) % 4
            
    
    if board[x][y] == 1:
        board[x][y] = 2
        snake.append([x, y])
    
    elif board[x][y] == 0:
        board[x][y] = 2
        snake.append([x, y])
        x2, y2 = snake.popleft()
        board[x2][y2] = 0
    
    else:
        break
        
print(answer)
    
    

# print(next_dir)
        
    
    