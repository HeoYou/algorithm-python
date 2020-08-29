x = int(input())

count = 99
if x < 100:
    print(x)
else:

    for n in range(100, x + 1):
        lst = []
        for i in range(len(str(n)) - 1):
            lst.append(int(str(n)[i]) - int(str(n)[i + 1]))
        lst = list(set(lst))
        if len(lst) == 1:
            count += 1

    print(count)

