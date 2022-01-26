def solution(board, skill):

    answer = 0

    for type, r1, c1, r2, c2, degree in skill:
        # print(type, r1, c1, r2, c2, degree)
        for i in range(r2 - r1 + 1):
            for j in range(c2 - c1 + 1):
                if type == 1:
                    board[i + r1][j + c1] -= degree
                else:
                    board[i + r1][j + c1] += degree
    for i in board:
        for j in i:
            if j > 0:
                answer += 1
    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))