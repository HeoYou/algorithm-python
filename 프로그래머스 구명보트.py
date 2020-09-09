def solution(people, limit):
    answer = 0
    
    while len(people) > 1:
        maxW = 0
        flag = False
        for i in range(1, len(people)):
            if people[0] + people[i] <= limit:
                maxW = max(maxW, people[i])
                flag = True
        answer += 1
        if flag:
            people.pop(0)
            people.remove(maxW)
        else:
            people.pop(0)
    if people:
        return answer + 1
    return answer

print(solution([70, 50, 80, 50], 100))