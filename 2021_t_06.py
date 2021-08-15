def solution(numOfStairs):
    answer = 1
    step = 1
    
    for i in range(1, numOfStairs):
        answer += step
        step += 1
    return answer

print(solution(5))