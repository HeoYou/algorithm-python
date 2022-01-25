from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 6)

answer = []

def dfs(info, tree, node, sheep, wolf, visit, visited):
    w = wolf
    s = sheep


    if info[node] == 1:
        w = wolf + 1
    else:
        s = sheep + 1
    if s > w:
        answer.append(s)
    else:
        return
    vd = deepcopy(visited)
    vd.append(node)
    v = deepcopy(visit)
    v = list(set(v).difference(vd))
    v.extend(tree[node])

    for i in v:
        dfs(info, tree, i, s, w, v, vd)




def solution(info, edges):
    tree = [[] for i in range(len(info))]
    for p, c in edges:
        tree[p].append(c)

    dfs(info, tree, 0, 0, 0, [], [])
        
    return max(answer)

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info, edges))