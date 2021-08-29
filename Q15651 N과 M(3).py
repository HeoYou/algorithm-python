# q15649 보다 느리네.. 좀 더 돌긴할듯
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

def bfs(lst):
    if len(lst) == m:
        print(' '.join(lst))
        return
    
    for i in range(1, n + 1):
        bfs(lst + [str(i)])

bfs([])

