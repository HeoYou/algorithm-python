n = int(input())

while True:
    nlst = list(map(str, str(n)))

    flag = True

    for i in nlst:
        if i in '01235689':
            flag = False
            break

    
    if flag:
        print(n)
        break

    n = n - 1