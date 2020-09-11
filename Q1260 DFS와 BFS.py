# import sys

# N, M, v = map(int, sys.stdin.readline().strip().split())

# graph = [[] for i in range(N + 1)]

# def dfs():
#     stack = [v]
#     visit = []

#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(sorted(graph[node],reverse = True))
#     return visit



# def bfs():
#     stack = [v]
#     visit = []

#     while stack:
#         node = stack.pop(0)
#         if node not in visit:
#             visit.append(node)
#             stack.extend(sorted(graph[node]))
#     return visit



# for i in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)

# dfsLst = dfs()
# bfsLst = bfs()

# print(" ".join(map(str,dfsLst)))
# print(" ".join(map(str, bfsLst)))

from collections import deque
import sys


def dfs(lst, n):
    stack = [n]
    visit = []

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(sorted(lst[node],reverse = True))
    return visit

def bfs(lst, n):
    stack = deque([n])
    visit = []

    while stack:
        node = stack.popleft()
        if node not in visit:
           visit.append(node)
           stack.extend(sorted(lst[node]))
    return visit



n, m, v = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfsAnswer = dfs(graph, v)
bfsAnswer = bfs(graph, v)
print(' '.join(map(str, dfsAnswer)))
print(' '.join(map(str, bfsAnswer)))


