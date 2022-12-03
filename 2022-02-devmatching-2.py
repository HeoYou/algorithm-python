def clean(flag, n, count):
    global rlt_map
    if flag:
        for i in range(n):
            rlt_map[n - 1][i] = count
            count += 1
        for i in range(n - 2, -1, -1):
            rlt_map[i][n - 1] = count
            count += 1
    else:
        for i in range(n):
            rlt_map[i][n - 1] = count
            count += 1
        for i in range(n - 2, -1, -1):
            rlt_map[n - 1][i] = count
            count += 1
    return count
        
        
        

rlt_map = []
def solution(n, horizontal):
    global rlt_map
    answer = [[]]
    
    rlt_map = [[0] * n for i in range(n)]
    rlt_map[0][0] = 1
    
    
    num = 2
    count = 2
    horizontal = not horizontal
    for i in range(n - 1):
        count = clean(horizontal, num, count)
        num += 1
        horizontal = not horizontal

    return rlt_map

print(solution(5, False))