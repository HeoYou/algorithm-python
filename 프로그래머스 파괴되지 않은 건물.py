# def solution(board, skill):

#     answer = 0

#     for type, r1, c1, r2, c2, degree in skill:
#         # print(type, r1, c1, r2, c2, degree)
#         for i in range(r2 - r1 + 1):
#             for j in range(c2 - c1 + 1):
#                 if type == 1:
#                     board[i + r1][j + c1] -= degree
#                 else:
#                     board[i + r1][j + c1] += degree
#     for i in board:
#         for j in i:
#             if j > 0:
#                 answer += 1
#     return answer

def solution(board, skill):

    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            tmp[r1][c1] = tmp[r1][c1] - degree
            tmp[r1][c2 + 1] = tmp[r1][c2 + 1] + degree
            tmp[r2 + 1][c1] = tmp[r2 + 1][c1] + degree
            tmp[r2 + 1][c2 + 1] = tmp[r2 + 1][c2 + 1] - degree
        if type == 2:
            tmp[r1][c1] = tmp[r1][c1] + degree
            tmp[r1][c2 + 1] = tmp[r1][c2 + 1] - degree
            tmp[r2 + 1][c1] = tmp[r2 + 1][c1] - degree
            tmp[r2 + 1][c2 + 1] = tmp[r2 + 1][c2 + 1] + degree
    for i in range(len(board)):
        for j in range(len(board[0])):
            tmp[i][j + 1] = tmp[i][j + 1] + tmp[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            tmp[i + 1][j] = tmp[i + 1][j] + tmp[i][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp[i][j]

    for i in board:
        for j in i:
            if j > 0:
                answer += 1
    return answer

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))