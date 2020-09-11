# import sys
# graph = {i + 1 : [] for i in range(int(sys.stdin.readline()))}

# def dfs(graph, start):
#     stack = [start]
#     visit = []

#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(graph[node])
#     return visit
# for i in range(int(sys.stdin.readline())):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
# answer = 0

# for i in range(len(graph)):
#     answer = max(answer, len(dfs(graph, i + 1)))

# print(answer - 1)

n = int(input())
l = int(input())

graph = [[] for i in range(n + 1)]
for i in range(l):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs():
    stack = [1]
    visit = []

    while stack:
        node = stack.pop()
        if node not in visit:
            stack.extend(graph[node])
            visit.append(node)

    return len(visit)

print(dfs() - 1)