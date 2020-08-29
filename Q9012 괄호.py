t = int(input())

for i in range(t):
    
    data = input()
    lst = [data[0]]
    if data[0] == ")":
        print("NO")
        continue

    for j in data[1:]:
        if j == "(":
            lst.append(j)
        else:
            if not lst:
                lst.append(j)
                break
            elif lst[-1] == "(":
                lst.pop()
    if not lst:
        print("YES")
    else:
        print("NO")

