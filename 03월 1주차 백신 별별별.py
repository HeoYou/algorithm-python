import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nodes = [[] for i in range(n + 1)]
visit = [0] * (n + 1)
answer = [0, 0]

for i in range(m):
    a, b = map(int, input().split())

    nodes[a].append(b)
    nodes[b].append(a)

print(nodes)

for i in range(1, n + 1):
    if visit[i] == 0:

        count = 1
        stack = [i]

        while stack:

            node = stack.pop()
            visit[node] = 1

            for j in nodes[node]:
                if visit[j] == 0:
                    visit[j] = 1
                    count += 1
                    stack.append(j)
            
        if answer[1] < count:
            answer[1] = count
            answer[0] = i

print(answer)