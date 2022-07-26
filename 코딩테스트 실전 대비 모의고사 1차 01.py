# def solution(X, Y):
    
#     answer = ''
#     numLst = []
    
#     X = sorted(list(map(int, X)))
#     Y = sorted(list(map(int, Y)))
    
#     x, y = 0, 0
#     xLen, yLen = len(X), len(Y)
#     while True:
#         if x >= xLen or y >= yLen:
#             break
        
#         if X[x] == Y[y]:
#             numLst.append(X[x])
#             x += 1
#             y += 1
#         elif X[x] > Y[y]:
#             y += 1
#         elif X[x] < Y[y]:
#             x += 1
#     return str(int(''.join(map(str, sorted(numLst, reverse=True))))) if numLst else "-1"

# print(solution("100", "203045"))

import pprint
def solution(X, Y):
    
    answer = []
    xDic, yDic = {str(i) : 0 for i in range(10)}, {str(i) : 0 for i in range(10)}
    
    for i in X:
        xDic[i] += 1
        
    for i in Y:
        yDic[i] += 1
    
    for i in xDic:
        for j in range(min(xDic[i], yDic[i])):
            answer.append(i)
    
    answer = sorted(answer, reverse=True)
    if not answer:
        return "-1"
    elif answer[0] == '0':
        return "0"
    else:
        return ''.join(answer)

print(solution("1100", "1101"))
