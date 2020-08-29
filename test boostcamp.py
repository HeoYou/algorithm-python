def solution(v):
    answer = []
    count1, count2 = [], []

    for i in range(3):
        count1.append(v[i][0])
        count2.append(v[i][1])
    count1 = sorted(count1)
    count2 = sorted(count2)
        
    if count1.count(count1[0]) == 1:
        answer.append(count1[0])
    else:
        answer.append(count1[2])


    if count2.count(count2[0]) == 1:
        answer.append(count2[0])
    else:
        answer.append(count2[2])

    return answer


v = [[1, 1], [2, 2], [1, 2]]
print(solution(v))
