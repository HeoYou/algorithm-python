from itertools import permutations

n = int(input())
inputList = list(map(int, input().split()))

lst = [i + 1 for i in range(n)]

combiLst = list(permutations(lst, n))

if list(combiLst[-1]) == inputList:
    print(-1)
else:
    for i in range(len(combiLst) - 1):
        if list(combiLst[i]) == inputList:
            print(' '.join(map(str, combiLst[i + 1])))
            
