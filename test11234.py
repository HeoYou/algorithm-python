lst = list(map(int, input()))

for i in range(1, len(lst)):
    lMul, rMul = 1, 1
    for j in lst[:i]:
        lMul *= j
    for j in lst[i:]:
        rMul *= j
    
    if lMul == rMul:
        print("YES")
        exit()
print("NO")
    
    