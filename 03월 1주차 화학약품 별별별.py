import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

answer = 0
n = int(input())
dataLst = list(map(int, input().strip().split(" ")))

def dfs(lst, pos, flag):
    global answer
    if flag and lst == 0:
        answer += 1
    if pos == n:
        return
    dfs(lst + dataLst[pos], pos + 1, True)
    dfs(lst, pos + 1, False)

dfs(0, 0, False)
print(answer)
