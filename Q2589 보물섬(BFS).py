n, m = map(int, input().split())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

lst = [list(input()) for _ in range(n)]

for x in range(n):
    for y in range(m):
        visit = [[0] * m for j in range(n)]
        for i in visit:
            print(i)
        stack = [[x, y, 1]]
        print(stack)
        
        while stack:
            sx, sy, d = stack.pop(0)
            visit[sx][sy] = d
            
            for i in range(4):
                nx, ny = sx + dx[i], sy + dy[i]
                if visit[x][y] == 0 and 0 <= x < n and 0 <= y < m:
                    stack.append(nx, ny, d + 1)
    for i in visit:
        print(i)
    print()



# def bfs(x, y, visit):

#     visit[x][y] = 0

#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if visit[x][y] and 0 <= x < n and 0 <= y < m:
#             bfs

