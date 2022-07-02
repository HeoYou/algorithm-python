import sys

sys.setrecursionlimit(10 ** 6)


answer = 0


N, K = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))

def dfs(visit, a, p, s):
    global answer
    answer = max(answer, s)
    
    for i in range(N):
        na = a * 2 + A[i]
        np = p - na
        ns = s + P[i]
        if np < 0:
            continue
        if i + 1 in visit:
            continue
        
        dfs(visit + [i], na, np, ns)
    
for i in range(N):
    if A[i] <= K:
        dfs([i], A[i], K - A[i], P[i])
        
print(answer)