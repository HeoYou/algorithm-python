# def solution(s):
#     answer = 10000
#     answerStr = ''
#     answerLst = []
#     if len(s) < 3:
#         return len(s)

#     for i in range(1, len(s) // 2 + 1):
#         if len(s) % i == 0:
#             count = 1
#             saveStr = s[:i]

#             for j in range(2, len(s)):

#                 print(s[i * (j - 1) : i * j])
#                 if saveStr == s[i * (j - 1) : i * j]:
#                     count += 1
#                 else:
#                     answerLst.append([count, saveStr])
#                     saveStr = s[i * (j - 1) : i * j]
#                     count = 1
#                 print(i, j, answerLst)
#             for count, S in answerLst:
#                 if count == 1:
#                     answerStr += S
#                 else:
#                     answerStr += str(count) + S
#             answer = min(answer, len(answerStr))
#             print(answerLst)
#             answerStr = ''
#             answerLst = []
#     return answer

# print(solution("aabbaccc"))

def solution(s):
    length = []
    result = ""
    
    if len(s) == 1:
        return 1
    
    for cut in range(1, len(s) // 2 + 1): 
        count = 1
        tempStr = s[:cut] 
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""
        
    return min(length)