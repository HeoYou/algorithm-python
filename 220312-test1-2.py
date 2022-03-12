import sys
sys.setrecursionlimit(10**6)

answer = [[]]
def tornado(nn, ts, s):
    global answer  
    if ts // 2 < s + 1:
        return  
    for i in range(ts - (s * 2) - 1):
        nn += 1
        answer[s][s + i] = nn
        answer[s + i][-s - 1] = nn
        answer[-s - 1][-s - 1 - i] = nn
        answer[-s - 1 - i][s] = nn
    
 
    if ts % 2 == 1:
        answer[ts // 2][ts // 2] = nn + 1

    tornado(nn, ts, s + 1)
    

def solution(n, clockwise):
    global answer
    
    answer = [[0] * n for _ in range(n)]
    tornado(0, n, 0)
    
    temp = [[0] * n for _ in range(n)]
    if not clockwise:
        for i in range(n):
            temp[i] = answer[n-1-i]
        return temp
    return answer

print(solution(9, False))