t = int(input())

for _ in range(t):

    n = int(input())
    a, b, c = 1, 2, 4
    flag = True
    for i in range(n - 1):
        if n == 1:
            flag = False
            print(1)
            break
        elif n == 2:
            flag = False
            print(2)
            break
        elif n == 3:
            flag = False
            print(4)
            break

        a, b, c = b, c, a + b + c
    if flag:
        print(a)
