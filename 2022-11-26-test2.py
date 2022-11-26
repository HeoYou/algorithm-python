# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque
def solution1(N, A, B):
    
    graph = list([] for i in range(N + 1))
    
    for a, b in zip(A, B):
        graph[a].append(b)
        graph[b].append(a)
    
    print(graph)
    
    q = deque([1])
    
    while q:
        node = q.popleft()
        
        

    print(False)
# solution(4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1])


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A, B):
    graph = list([] for i in range(N + 1))
    
    for a, b in zip(A, B):
        if abs(a - b) == 1:
            graph[a].append(b)
            graph[b].append(a)
    
    # print(graph)
    if graph[1] and graph[N] and graph[1][0] == 2 and graph[N][0] == N - 1:
        for lst in graph[2:-1]:
            if len(lst) != 2:
                return False
        return True
    else:
        return False
   

solution(4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1])
solution(4, [1, 2, 1, 3], [2, 4, 3, 4])
solution(6, [2, 1, 4, 5, 3], [3, 3, 5, 6, 4])


