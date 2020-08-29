n = int(input())

tree = {i + 1 : [] for i in range(n)}
lst = [[0, 0] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().strip().split(" "))
    tree[a].append(b)
    tree[b].append(a)
a, b = list(map(int, input().split(" ")))

def dfs(startNode):
    visit = []
    stack = [startNode]
    global lst

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            while len(tree[node]) > 0:
                childrenNode = tree[node].pop()
                if childrenNode not in visit:
                    lst[childrenNode][1] = lst[node][1] + 1
                    lst[childrenNode][0] = node    
                    stack.append(childrenNode)

def find(a, b):
    for i in range(n):
        if a == b:
            return a
    
        if lst[a][1] > lst[b][1]:
            a = lst[a][0]
        elif lst[a][1] < lst[b][1]:
            b = lst[b][0]
        else:
            a = lst[a][0]
            b = lst[b][0]

    

dfs(1)
print(find(a,b))

