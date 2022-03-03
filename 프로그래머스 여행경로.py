def solution(tickets):
    graph = {}

    for t in tickets:
        if graph.get(t[0]):
            graph[t[0]].append(t[1])
        else:
            graph[t[0]] = [t[1]]
        if not graph.get(t[1]):
            graph[t[1]] = []

    for i in graph.keys():
        graph[i] = sorted(graph[i], reverse = True)
        
    answer = []

    s = ["ICN"]
    while s:
        node = s[-1]
        if not graph[node]:
            answer.append(s.pop())
        else:
            s.append(graph[node].pop())

    answer.reverse()
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))