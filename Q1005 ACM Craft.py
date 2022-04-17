import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    
    node, edge = map(int, input().split())
    
    graph = [[] for _ in range(node + 1)]
    inCount = [0] * (node + 1)
    
    nodes = [0] + list(map(int, input().split()))
    
    
    for i in range(edge):
        a, b = map(int, input().split())
        
        graph[a].append(b)
        inCount[b] += 1
    
    W = int(input())
    
    
    answer = [0] * (node + 1)
    q = deque()
    
    for i in range(1, node + 1):
        if inCount[i] == 0:
            q.append(i)
            answer[i] += nodes[i]
            
    
    while q:
        n = q.popleft()
        
        for i in graph[n]:
            inCount[i] -= 1
            answer[i] = max(answer[i], answer[n] + nodes[i])
            
            if  inCount[i] == 0:
                q.append(i)
        
        if inCount[W] == 0:
            print(answer[W])
            break
   
# from collections import defaultdict, deque

# def topology_sort():
#     DP_table = [0] * (N+1)

#     q = deque()

#     for i in range(1, N+1):
#         if in_degree[i] == 0:
#             q.append(i)
#             DP_table[i] += time_list[i]

#     while q:
#         now = q.popleft()

#         for i in graph[now]:
#             in_degree[i] -= 1
#             DP_table[i] = max(DP_table[i], DP_table[now] + time_list[i])

#             if in_degree[i] == 0:
#                 q.append(i)

#     print(DP_table)
#     return DP_table[target]
    
    
# T = int(input())

# for test_case in range(T):

#     N, K = map(int, input().split())
#     time_list = [0] + list(map(int, input().split()))
#     graph = [[] for _ in range(N+1)]
#     in_degree = [0] * (N+1)

#     for _ in range(K):
#         start, end = map(int, input().split())
#         graph[start].append(end)
#         in_degree[end] += 1

#     print(graph)
#     target = int(input())

#     print(topology_sort())