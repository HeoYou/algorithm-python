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
    if d == 5:
        print(1)
        exit()
    
    for i in node[num]:
        if visit[i] == 0:
            dfs(d + 1, i)

for i in range(n):
    visit = [0] * n
    dfs(1, i)
print(0)
