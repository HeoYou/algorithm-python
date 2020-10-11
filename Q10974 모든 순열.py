from itertools import permutations

n = int(input())

lst = [i + 1 for i in range(n)]

combiLst = list(permutations(lst, n))
for i in combiLst:
    print(' '.join(map(str, i)))