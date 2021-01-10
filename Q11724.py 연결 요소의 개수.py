import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]

answer = 0

def dfs(node):
    visit[node] = True
    # print(visit)
    for i in graph[node]:
        if not visit[i]:
            dfs(i)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

for i in range(1, N + 1):

    if not visit[i]:
        #print(1234,visit)
        answer += 1
        dfs(i)

print(answer)

