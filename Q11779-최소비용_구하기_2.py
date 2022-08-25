import heapq
import sys

input = sys.stdin.readline

N= int(input())
m = int(input())

visit = [float('inf') for i in range(N + 1)]


graph = [[] for _ in range(N + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
  
start, end = map(int, input().split())

visit = [float('inf') for i in range(N + 1)]
visit[start] = 0
path = [[] for i in range(N + 1)]
path[start].append(start)
h = []
heapq.heappush(h, [0, start])

while h:
    now_dis, now_node = heapq.heappop(h)
    
    print("123  ", now_dis, now_node)
    
    if now_dis > visit[now_node]:
        continue
        
    for next_node, next_dis in graph[now_node]:
        path_dis = next_dis + visit[now_node]
        if path_dis < visit[next_node]:
            visit[next_node] = path_dis
            heapq.heappush(h, [path_dis, next_node])
            path[next_node] = path[now_node] + [next_node]

print(visit[end])
print(len(path[end]))
print(' '.join(map(str, path[N])))
    
    
    

