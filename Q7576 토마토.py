# import copy
# import sys
# input = sys.stdin.readline
# M, N = map(int, input().split())
# data = []
# answer = -1
# dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

# for i in range(N):
#     data.append(list(map(int, input().split())))
# tmpData = copy.deepcopy(data)


# def tomato(x, y):
#     global data

#     for i in range(4):
#         xx, yy = x + dx[i], y + dy[i]

#         if xx < 0 or xx >= N or yy < 0 or yy >= M or data[xx][yy] == -1:
#             continue
#         if tmpData[xx][yy] == 0:
#             data[xx][yy] = 1




# while True:
#     answer += 1
#     for i in range(N):
#         for j in range(M):
#             if tmpData[i][j] == 1:
#                 tomato(i, j)
    

#     if data[:] == tmpData[:]:
#         for i in data:
#             if 0 in i:
#                 print(-1)
#                 exit()
#             else:
#                 print(answer)
#                 exit()

#     tmpData = copy.deepcopy(data)



import copy
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
data = []
answer = -1
back_count = 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(N):
    data.append(list(map(int, input().split())))
tmpData = copy.deepcopy(data)
for i in data:
    for j in i:
        if j == 0:
            back_count += 1


def tomato(x, y):
    global data

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]

        if xx < 0 or xx >= N or yy < 0 or yy >= M or data[xx][yy] == -1:
            continue
        if tmpData[xx][yy] == 0:
            data[xx][yy] = 1

while True:
    answer += 1
    for i in range(N):
        for j in range(M):
            if tmpData[i][j] == 1:
                tomato(i, j)
    
    count = 0
    for i in data:
        for j in i:
            if j == 0:
                count += 1
    if count != back_count:
        tmpData = copy.deepcopy(data)
        back_count = count
        continue
    else:
        if count == 0:
            print(answer)
            break
        else:
            print(-1)
            break
        
