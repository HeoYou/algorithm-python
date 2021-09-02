def solution(scores):
    
    answer = []
    for i in range(len(scores)):
        if scores[i][i] == max(scores[i]) or scores[i][i] == min(scores[i]):
            if scores[i].count(scores[i][i]) == 1:
                print(1123)
                answer.append((sum(scores[i]) - scores[i][i]) / (len(scores) - 1))
        else:
            print(scores[i])
            answer.append(sum(scores[i]) / (len(scores[i])))
    return answer
print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))


a = [1, 2, 3, 4, 4]
print(a.count(4))