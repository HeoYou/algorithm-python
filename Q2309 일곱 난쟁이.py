dwarf = sorted([int(input()) for _ in range(9)])
height = sum(dwarf)
flag = False
for i in range(8):
    for j in range(i + 1, 9):
        if height - dwarf[i] - dwarf[j] == 100:
            flag = True
            for x in range(9):
                if dwarf[x] != dwarf[i] and dwarf[x] != dwarf[j]:
                    print(dwarf[x])
                
    if flag:
        break