def solution(grade):
    answer = 0
    
    for i in range(len(grade) - 2, -1, -1):
        if grade[i] <= grade[i + 1]:
            continue
        answer -= grade[i + 1] - grade[i]
        grade[i] = grade[i + 1]
    
    return answer

print(solution([3, 2, 3, 6, 4, 5]))