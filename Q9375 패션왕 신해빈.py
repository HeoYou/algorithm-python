t = int(input())

for _ in range(t):
    n = int(input())
    wear = {}
    for i in range(n):
        a, b = map(str, input().split())
        if b in wear.keys():
            wear[b] += 1
        else:
            wear[b] = 1


    if len(wear) == 1:
        print(list(wear.values())[0])
    else:
        num = 1
        for j in list(wear.values()):
            num = num * (j + 1)
        print(num - 1)