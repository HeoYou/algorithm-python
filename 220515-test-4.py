import pprint

answer = [[0] * 6 for i in range(6)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def put_macaron(loc, color):
    global answer
    for i in range(5, -1, -1):
        if answer[i][loc] == 0:
            answer[i][loc] = color
            return i, loc
        
def delete(x, y):
    global answer
    lst = [[x, y]]
    stack = [[x, y]]
    color = answer[x][y]
    
    while stack:
        x, y = stack.pop()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= 6 or ny < 0 or ny >= 6 or color != answer[nx][ny]:
                continue
            if [nx, ny] in lst:
                continue
            stack.append([nx, ny])
            lst.append([nx, ny])
            
    if len(lst) >= 3:
        for x, y in lst:
            answer[x][y] = 0
            
            
def down():
    flag = False
    for i in range(5, 0, -1):
        for j in range(6):
            if answer[i][j] == 0 and answer[i - 1][j] != 0:
                flag = True
                answer[i][j] = answer[i - 1][j]
                answer[i - 1][j] = 0
    return flag


            
def solution(macaron):
    
    for loc, color in macaron:
        put_macaron(loc - 1, color)
        while True:
            for i in range(6):
                for j in range(6):
                    if answer[i][j] == 0:
                        continue
                    delete(i, j)
            if not down():
                break
    pprint.pprint(answer)
    return [''.join(map(str, i)) for i in answer]

# print(solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]) == ["000000","000000","000000","000000","000000","204004"])
print("test")
answer = [[0] * 6 for i in range(6)]
pprint.pprint(solution([[1,1],[6,5],[6,5],[6,5],[6,5],[6,5],[6,4],[6,1],[6,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]) == ["000000","000000","000000","000000","000000","404001"])