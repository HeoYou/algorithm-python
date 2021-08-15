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

# n, m = map(int, input().split(' '))
# lst = []
# answer = []
# for i in range(n):
#     lst.append(input())
# wb, bw = 'WB', 'BW'

# for i in range(n - 7):
#     for j in range(m - 7):
#         w, b = 0, 0
#         for x in range(i, i + 8):
#             for y in range(j, j + 8):
#                 if (x + y) % 2 == 0:
#                     if lst[x][y] != 'W': w += 1  
#                     if lst[x][y] != 'B': b += 1
#                 else:
#                     if lst[x][y] != 'B': w += 1  
#                     if lst[x][y] != 'W': b += 1
#     answer.append(w)  
#     answer.append(b)

# print(min(answer))


n, m = map(int, input().split())
l = []
mini = []

for _ in range(n):
    l.append(input())

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8): 
                if (j + b)%2 == 0:
                    if l[b][j] != 'W': idx1 += 1  
                    if l[b][j] != 'B': idx2 += 1
                else :
                    if l[b][j] != 'B': idx1 += 1
                    if l[b][j] != 'W': idx2 += 1
        mini.append(idx1)                        
        mini.append(idx2)                          

print(min(mini))  
















