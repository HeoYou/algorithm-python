import heapq

n, m = map(int, input().split())

visit = [0] * (n + 1)
answer = 0
h = []
for i in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(h, [c, a, b])

for i in range(m):
    c, a, b = heapq.heappop(h)
    if visit[a] == 0 or visit[b] == 0:
        visit[a] = 1
        visit[b] = 1
        answer += c

print(answer)