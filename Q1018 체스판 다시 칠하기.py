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



import sys


















