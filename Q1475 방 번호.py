n = input()

lst = [0 for i in range(9)]
for i in n:
    if i == "9":
        lst[6] += 1
    else:
        lst[int(i)] += 1
lst[6] = (lst[6] + 1) // 2
print(max(lst))
