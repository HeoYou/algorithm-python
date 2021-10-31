def solution(N, road, K):
    answer = 0

    graph = [{} for i in range(N + 1)]

    for r in road:
        if graph[r[0]].get(r[1]) == None:
            graph[r[0]][r[1]] = r[2]
        else:
            if graph[r[0]][r[1]] > r[2]:
                graph[r[0]][r[1]] = r[2]

        if graph[r[1]].get(r[0]) == None:
            graph[r[1]][r[0]] = r[2]
        else:
            if graph[r[1]][r[0]] > r[2]:
                graph[r[1]][r[0]] = r[2]

    
    queue = [1]
    visit = [99999999] * (N + 1)
    visit[1] = 0

    while queue:

        node = queue.pop(0)
        
        for i in graph[node].keys():
            if visit[i] >= visit[node] + graph[node][i]:
                queue.append(i)
                visit[i] = visit[node] + graph[node][i]

    for i in visit:
        if i <= K:
            answer += 1
    return answer


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))