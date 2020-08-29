import copy

def solution(m, n, board):

    copyBoard = [list(board[i]) for i in range(m)]
    board = copy.deepcopy(copyBoard)
    while True:
        copyBoard = copy.deepcopy(board)
        for i in range(m - 1):
            for j in range(n):
                copyBoard = search(i, j, board, copyBoard)
        copyBoard = downBoard(m, n, copyBoard)
        if copyBoard == board:
            break
        else:
            board = copyBoard
    answer = 0
    for i in range(m):
        answer += board[i].count("0")

    return answer

def search(x, y, b, copyB):
    dx, dy = [1, 1, 0], [0, 1, 1]
    chk = b[x][y]
    flag = True

    for i in range(3):
        xx, yy = x + dx[i], y + dy[i]
        if yy < len(b[0]):
            if chk != b[xx][yy]:
                flag = False
                break

    dx, dy = [0, 1, 1, 0], [0, 0, 1, 1]
    if flag:
        for i in range(4):
            if yy < len(b[0]):
                xx, yy = x + dx[i], y + dy[i]
                copyB[xx][yy] = "0"

    return copyB

# 반복문 구간과 숫자 0 문자 "0" 을 구분하는걸 생각하지 못해서 많은 시간을 보냄
def downBoard(m, n, board):
    copyBoard = []
    while True:
        if copyBoard == board:
            return board
        else:
            copyBoard = copy.deepcopy(board)            
        for i in range(m - 1, 0, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "0":
                    board[i][j] = board[i - 1][j]
                    board[i - 1][j] = "0"




print(solution(4, 5,["CCBDE", "AAADE", "AAABF", "CCBBF"] ))