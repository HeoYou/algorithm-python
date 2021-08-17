# 문제 다시한번 풀어보려고 들어왔는데
# 왜 이딴식으로 풀어논지 전혀 감이 안잡힌다.

# def solution(gems):
#     answer = []
#     start, end = 0, 0
#     gemCount = len(set(gems))

#     while len(set(gems[start:end])) != gemCount:
#         end += 1
    
#     while len(set(gems[start:end])) == gemCount:
#         start += 1


#     return [start, end]

def solution(gems):
    answer = []
    left, right = 0, 0
    total = len(gems)
    dic = {}
    for i in set(gems):
        dic[i] = 0
    dic[gems[0]] += 1
    print(dic)

    while right != total - 1:

        if min(dic.values()) == 0:
            right += 1
            dic[gems[right]] += 1

        else:
            answer.append([left + 1, right + 1, right - left])
            dic[gems[left]] -= 1
            left += 1
        print(dic, left, right)
    answer = sorted(answer, key = lambda x : x[2])
    return [answer[0][0], answer[0][1]] if len(answer) else [1, len(gems)]


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))