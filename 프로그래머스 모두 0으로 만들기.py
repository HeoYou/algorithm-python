import sys
sys.setrecursionlimit(10**6)
v = []
answer = 0
visit = {}
def dfs(tree, node):
    global v
    global answer
    global visit

    visit[node] = 1
    
    if 1 == len(tree[node]):
        answer += v[node]
        return v[node]
    for i in tree[node]:
        if visit.get(i):
            continue
        val = dfs(tree, node)
        v[node] += val
    

def solution(a, edges):
    global answer
    global v
    v = a
    if not sum(a) == 0:
        return -1
    

    tree = [[] for i in range(len(a))]
    parent = [-1 for i in range(len(a))]
    leaf = []
    for node in edges:
        tree[node[0]].append(node[1])
        tree[node[1]].append(node[0])

    dfs(tree, 0)
    stack = [0]
    visit = {}
    
    # while stack:

    #     node = stack.pop()

    #     if 1 == len(tree[node]):
    #         leaf.append(node)
    #     for i in tree[node]:
    #         if visit.get(i):
    #             continue
    #         parent[i] = node
    #         stack.append(i)
    #         visit[i] = 1
    # print(parent)
    # print(leaf)
    # print(a, answer)
    # for i in leaf:
    #     node = i
    #     while node != 0:
    #         print(node, a, answer)
    #         answer += abs(a[node])
    #         a[parent[node]] += a[node]
    #         a[node] = 0
    #         node = parent[node]
    #         print(node, a, answer)
    #         print()

    return answer


if __name__ == "__main__":

    a = [-2, 8, -5, -5, -3, 0, 5, 2]
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]]

    print(solution(a, edges))