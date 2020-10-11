def solution(n):
    answer = 0
    sum = 0
    top, bottom = 0, 0
    while bottom <= (n + 1) // 2:
        if sum == n:
            answer += 1
            top += 1
            sum += top
        elif sum < n:
            top += 1
            sum += top
        elif sum > n:
            sum -= bottom
            bottom += 1

    return answer + 1

print(solution(15))