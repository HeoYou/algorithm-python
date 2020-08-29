n = int(input())

lst = []
ans = []

for i in range(n):
    lst.append(input())

ans = list(lst[0])

for i in range(len(lst[0])):

    for j in range(1, n):
        if ans[i] != lst[j][i]:
            ans[i] = "?"

    
print(''.join(ans))