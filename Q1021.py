n, m = map(int, input().split(" "))

poplst = list(map(int, input().split(" ")))

lst = [i + 1 for i in range(n)]
count = 0


while len(poplst) > 0:

    if poplst[0] == lst[0]:
        poplst.pop(0)
        lst.pop(0)
    elif lst.index(poplst[0]) < (len(lst) + 2) // 2:
        count += 1
        lst.append(lst.pop(0))
    else:
        count += 1
        lst.insert(0, lst.pop(-1))


print(count)