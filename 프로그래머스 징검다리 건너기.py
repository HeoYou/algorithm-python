def solution(s, k):
    answer = 2000000000
    if len(s) == k:
        return max(s)
    for i in range(len(s) - k):
        answer = min(answer, max(s[i : i + k]))
    return answer

print(solution([0, 0, 5],3))