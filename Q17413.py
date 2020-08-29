s, tmp = input(), ""

ck = False
for i in S:

    if i == ' ':
        if not ck:
            print(tmp[::-1], end=" ")
        else:
            print(" ", end=" ")

    elif i in '<': #꺽쇠
        ck = True
        print("<", end="")

    elif i in '>': 
        ck = Flase
        print(">", end="")

    else: #알파벳과 숫자