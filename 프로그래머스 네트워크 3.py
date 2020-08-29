def solution(n, computers):
    answer = []
    graph = {i : [] for i in range(n)}

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                graph[i].append(j)

    def dfs(start):
        nonlocal graph
        visit = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visit:
                visit.append(node)
                stack.extend(graph[node])
        return visit
        
    for i in range(n):
        answer.append(dfs(i))

    return len(list(set(map(tuple, [sorted(i) for i in answer]))))

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(3, computers))