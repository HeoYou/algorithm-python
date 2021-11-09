def solution(n, wires):

    tree = makeTree(n, wires)
    answer = 100000

    for a, b in wires:

        answer = min(answer, abs(dfs(n, a, b, tree) - dfs(n, b, a, tree)))

    return answer

def makeTree(n, wires) -> list:
    tree = [[] for _ in range(n + 1)]
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
    return tree

def dfs(n, root, cut_node, tree):
    count = 0
    visit = [0] * (n + 1)
    visit[cut_node] = 1
    stack = [root]
    while stack:
        count += 1
        node = stack.pop()
        visit[node] = 1
        
        for i in tree[node]:
            if visit[i] == 0:
                stack.append(i)
    return count

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))