n, m = map(int, input().split())
count = 1

if m % n:
    print(-1)
    exit()

else:
    m = m // n
    while True:

        if m % 2 == 0:
            m = m // 2
            count += 1
        elif m % 3 == 0:
            m = m // 3
            count += 1
        else:
            break
if m == 1:
    print(count)
else:
    print(-1)