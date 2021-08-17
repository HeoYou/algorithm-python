# 옛날에 짯던 코드인데 이방법으로 안되는게 확실하다
# 아마 다른도시를 거쳐 갈 수 있다는걸 간과한 결과인거같은데
# 금방 풀 수 있을것 같다

# import sys

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# city = []
# root = []

# for _ in range(n):
#     city.append(list(map(int, sys.stdin.readline().split())))
# root = list(map(int, sys.stdin.readline().split()))

# flag = True

# for i in range(m - 1):
#     if root[i] == root[i + 1]:
#         continue
#     if city[root[i] - 1][root[i + 1] - 1] == 0:
#         falg = False
#         break
# if flag:
#     print("YES")
# else:
#     print("NO")


# 첫번째 방문지를 기준으로 그래프 탐색을 한다
# 그래프로 탐색한 곳을 기록하고 나중에 체크하는 식으로


# 엣지 케이스가 나온 것 같다 안풀리네
import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
graph = [[] for i in range(n + 1)]
visit = [0] * (n + 1)

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j]:
            graph[i + 1].append(j + 1)

lst = list(map(int, input().split()))

stack = [lst[0]]

while stack:

    node = stack.pop()
    visit[node] = 1

    for i in graph[node]:
        if visit[i] == 0:
            stack.append(i)

for i in lst:
    if visit[i] == 0:
        print('NO')
        break
print('YES')



