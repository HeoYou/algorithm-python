# 이걸 통과하네... 시간제한 걸릴줄

import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

def bfs(lst):
    if len(lst) == m:
        print(' '.join(lst))
        return
    
    for i in range(1, n + 1):
        # in에서 걸릴줄 알았는데
        if str(i) not in lst:
            bfs(lst + [str(i)])

bfs([])

