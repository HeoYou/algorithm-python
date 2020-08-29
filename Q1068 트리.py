num = int(input())
lst = list(map(int, input().split()))
deleteNode = int(input())
count = 0

tree = {i : [] for i in range(num)}
root = 0

def dfs(delete):
    global tree
    stack = [delete]

    while stack:
        node = stack.pop()

        if tree[node] == []:
            tree[node].append(100)
        else:
            stack.extend(tree[node])

for i in range(num):
    if lst[i] != -1:
        tree[lst[i]].append(i)
    else:
        root = i
print(tree)
dfs(deleteNode)

for i in range(num):
    if tree[i] == [deleteNode]:
        tree[i] = []

for i in range(num):
    if tree[i] == []:
        count += 1

print(count)

# 자식 노드가 한개일경우에서 자식노드를 삭제했을 때 예외처리 X
# 부모노드가 리프노드가 되게끔 해야한다.