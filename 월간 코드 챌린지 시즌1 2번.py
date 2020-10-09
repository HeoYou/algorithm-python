def checkNum(arr):
    numTmp = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if numTmp != arr[i][j]:
                return False, numTmp
    return True, numTmp

def process(arr):

    size = len(arr) // 2
    
    flag, num = checkNum([arr[i][:size]for i in range(size)])

    if flag:
        answer[num] += 1
    else:
        process([arr[i][:size]for i in range(size)])

    flag, num = checkNum([arr[i][size:]for i in range(size)])

    if flag:
        answer[num] += 1
    else:
        process([arr[i][size:]for i in range(size)])

    flag, num = checkNum([arr[i][:size]for i in range(size, len(arr))])

    if flag:
        answer[num] += 1
    else:
        process([arr[i][:size]for i in range(size, len(arr))])

    flag, num = checkNum([arr[i][size:]for i in range(size, len(arr))])

    if flag:
        answer[num] += 1
    else:
        process([arr[i][size:]for i in range(size, len(arr))])


answer = [0, 0]
def solution(arr):
    flag, num = checkNum(arr)
    if flag:
        answer[num] += 1
        return answer
    process(arr)
    return answer


print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))