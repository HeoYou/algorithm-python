import sys
input = sys.stdin.readline

n = int(input())

answer = [0] * (n + 1)
visit = [0] * (n + 1)

graph = [[] for i in range(n + 1)]
stack = []

for i in range(n - 1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
stack = [1]
visit[1] = 1
while stack:

    node = stack.pop()
    for i in graph[node]:
        if visit[i] == 0:
            visit[i] = 1
            answer[i] = node
            stack.append(i)

for i in answer[2:]:
    print(i)
