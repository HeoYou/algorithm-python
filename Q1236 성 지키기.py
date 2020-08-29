# import copy

# C, R = map(int, input().split())

# emptyC, emptyR = 0, 0

# def chk(lst, n):
#     count = 0
#     for i in range(n):
#         if "X" not in lst[i]:
#             count += 1
#     return count

# def rotate90(lst):
#     newLst = [[0 for _ in range(len(lst))] for _ in range(len(lst[0]))]
#     print(newLst)
#     for i in range(len(lst)):
#         for j in range(len(lst[0])):
#             newLst[i][j] = lst[j][len(lst)-i-1]
#     return newLst

# lst = list(list(input()) for i in range(C))
# print(rotate90(lst))

# print(chk(lst, C))
# print(lst)

C, R = map(int, input().split())
emptyC, emptyR = 0, 0
lst = list(list(input()) for i in range(C))

for i in range(C):
    if 'X' not in lst[i]:
        emptyC += 1
    
for i in range(R):
    flag = True
    for j in range(C):
        if lst[j][i] == 'X':
            flag = False
    if flag:
        emptyR += 1

print(min(emptyC, emptyR))

