import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

lst = sorted(list(map(int, input().split())))


def bfs(subLst, nn):
    if len(subLst) >= m:
        print(' '.join(map(str, subLst)))
        return
    
    for i in range(n):
        if nn == i or lst[i] in subLst:
            continue
        bfs(subLst + [lst[i]], i)
       
       
for i in range(n): 
    bfs([lst[i]], i)