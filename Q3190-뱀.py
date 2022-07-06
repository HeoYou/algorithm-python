import heapq
from collections import deque

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

N = int(input())

board = [[2] + [0] * (N) + [2] for i in range(N)]
board = [[2] * (N + 2)]+ board + [[2] * (N + 2)]
print(board)

next_dir = deque()
snake = deque([1, 1])
direction = 1   # 0위 1오 2아래 3왼

for i in range(K := int(input())):
    a, b = map(int, input().split())
    
    board[a][b] = 1

for i in range(int(input())):
    a, b = input().split()
    next_dir.append([int(a), b])
    
for i in board:
    print(i)
    
x, y = 1, 1
answer = 0

# while True:
#     answer += 1
#     x, y = x + dx[direction], y + dy[direction]
    
#     if board[x][y] == 1:
        
    
    
    

# print(next_dir)
        
    
    