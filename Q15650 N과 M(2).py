import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

def bfs(lst):
    if len(lst) == m:
        print(' '.join(lst))
        return
    
    for i in range(int(lst[-1]) + 1, n + 1):
        bfs(lst + [str(i)])

for i in range(1, n + 1):
    bfs([str(i)])

