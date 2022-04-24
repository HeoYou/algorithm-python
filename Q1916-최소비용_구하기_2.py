import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())


distance = [INF] * (n + 1)

graph = [[] for i in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):

  q = []

  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:

    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for l in graph[now]:
      cost = dist + l[1]

      if cost < distance[l[0]]:

        distance[l[0]] = cost
        heapq.heappush(q, (cost, l[0]))

dijkstra(start)

print(distance[end])