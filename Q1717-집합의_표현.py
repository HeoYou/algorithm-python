import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [ i for i in range(n + 1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
    	return
    if x < y:
    	parent[y] = x
    else:
    	parent[x] = y
    
for _ in range(m):
    a, b, c = map(int, input().split())
    
    if a == 0:
        union(b, c)
        
    else:
        if find(b) == find(c):
        	print("YES")
        else:
        	print("NO")
