from itertools import combinations 

while True:
    items = list(map(int, input().split()))
    if len(items) == 1:
        break
    del [0]
    lst = sorted(list(combinations(items, 6)))
    for i in lst:
        for j in sorted(list(i)):
            print(j, end=' ')
        print()
    print()