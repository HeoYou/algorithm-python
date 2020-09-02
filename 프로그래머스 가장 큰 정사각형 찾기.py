def solution(board):
    answer = 1
    nx, ny = len(board), len(board[0])
    if nx == 1 or ny == 1:
        return 1

    for x in range(nx - 1):
        for y in range(ny - 1):
            if board[x][y] == 1:
                flag = True
                num = 0
                minN = min(nx - x - 1, ny - y - 1)
                for i in range(1, minN + 1):
                    num = i + 1
                    for j in range(0, minN + 1):
                        # print(x, y, i, board[x + j][y : y + i + 1])
                        if 0 in board[x + j][y : y + i + 1]: 

                            flag = False
                            break
                if flag:
                    answer = max(answer, num)


    return answer ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))



# def solution(board):
#     answer = 0

#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             flag = True
#             endPoint = 0

#             if board[i][j] == 1:
#                 while True:
#                     endPoint += 1

#                     if i + endPoint < len(board) and j + endPoint < len(board[0]):
#                         for k in range(endPoint + 1):
#                             if board[i + k][j + endPoint] != 1 and board[i + endPoint][j + k] != 1:
#                                 flag = False
#                                 break
#                     else:
#                         flag = False
#                         break
#                     if flag:
#                         answer = max(answer, (endPoint + 1) ** 2 )
#                     elif not flag:
#                         break

#             else:
#                 continue
                

#     return answer