import sys

sys.setrecursionlimit(10 ** 6)

def dfs(x):
    global ans
    global visit
    
    visit[x] = True
    cycle.append(x)
    
    num = lst[x]
    
    if visit[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    
    else:
        dfs(num)
    
    
for _ in range(int(input())):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    
    ans = []
    visit = [False] * (n + 1)
    
    for i in range(1, n + 1):
        
        if not visit[i]:
            cycle = []
            dfs(i)
    
    print(n - len(ans))
            