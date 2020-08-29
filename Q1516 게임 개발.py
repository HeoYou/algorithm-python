n = int(input())

lst = [list(map(int, input().strip().split()))]
lst[0].append(lst[0][0])
print(lst[0][0])

for i in range(1, n):
    lst.append(list(map(int, input().strip().split())))
    time = lst[i][0]
    answer = []
    if len(lst[i]) <= 2:
        print(time)
    else:
        for j in range(1, len(lst[i]) - 1):
            answer.append(lst[lst[i][j] - 1][-1])
        time += max(answer)
        print(time)
    lst[i].append(time)
    
print(lst)