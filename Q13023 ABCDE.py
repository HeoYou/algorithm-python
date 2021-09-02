# n, m = map(int, input().split())

# node = [[] for i in range(n)]
# visit = [0] * n
# for i in range(m):
#     x, y = map(int, input().split())
#     node[x].append(y)
#     node[y].append(x)


# for i in range(n):
#     if visit[i] == 0:
#         stack = [i]
#         count = 0
#         while stack:
#             print(stack)
#             n = stack.pop()
#             visit[n] = 1
#             count += 1
#             if count >= 5:
#                 print(1)
#                 exit()
#             for j in node[n]:
#                 if visit[j] == 0:
#                     stack.append(j)
    
# print(0)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

node = [[] for i in range(n)]
visit = [0] * n
for i in range(m):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)

def dfs(d, num):
    global visit
    visit[num] = 1
    if d == 4:
        print(1)
        exit()
    
    for i in node[num]:
        if visit[i] == 0:
            visit[i] = True
            dfs(d + 1, i)
            visit[i] = False

for i in range(n):
    visit[i] = True
    dfs(0, i)
    visit[i] = False
print(0)

