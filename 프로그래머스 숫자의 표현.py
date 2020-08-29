def solution(n):
    answer = 1

    num = [i for i in range((n + 4) // 2)]
    start, end = 0, 1
    while start < (n + 2) // 2 :
        if sum(num[start:end]) == n:
            answer += 1
            start += 1
            end += 1
        elif sum(num[start:end]) > n:
            start += 1
        elif sum(num[start:end]) < n:
            end += 1

    return answer

print(solution(15))

# return len([i  for i in range(1,num+1,2) if num % i is 0])