# import sys

# n, m = map(int, sys.stdin.readline().split(" "))
# wb = "WB"
# lst = []
# minCountW, minCountB = 10001, 10001

# for i in range(n):
#     lst.append(sys.stdin.readline())
# for x in range(n - 7):
#     for y in range(m - 7):
#         countW, countB = 0, 0
#         for i in range(8):
#             for j in range(8):
#                 if lst[i + x][j + y] != wb[(i + j) % 2]:
#                     countW += 1
#                 if lst[i + x][j + y] != wb[(i + j + 1) % 2]:
#                     countB += 1
#     minCountW = min(minCountW, countW)
#     minCountB = min(minCountB, countB)

# print(min(minCountB, minCountW))

n, m = map(int, input().split(' '))
lst = []
ansW, ansB = 100000, 100000
for i in range(n):
    lst.append(input())
wb, bw = 'WB', 'BW'
for i in range(n - 7):
    for j in range(m - 7):
        w, b = 0, 0
        for x in range(8):
            for y in range(8):
                if lst[i + x][j + y] != wb[(i + j + x + y) % 2]:
                    w += 1
                if lst[i + x][j + y] != bw[(i + j + x + y) % 2] :
                    b += 1
    ansW, ansB = min(ansW, w), min(ansB, b)  

print(min(ansW, ansB))


















