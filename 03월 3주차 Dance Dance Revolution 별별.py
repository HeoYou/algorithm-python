N = int(input())

lst = {}
flag = True

for i in range(N):
    n, m = map(int, input().split())
    if m not in lst:
        lst[m] = 1
    else:
        lst[m] += 1
    if lst[m] >= 3:
        flag = False
        break

if flag == True:
    print(1)
else:
    print(0)



