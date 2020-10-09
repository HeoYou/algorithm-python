def solution(s):
    answer = 0
    maxN = 0
    for i in range(len(s)):
        maxN = 0
        for j in range(i, len(s)):

            if s[i] != s[j]:
                answer += j - i
                maxN = j - i
            else:
                answer += maxN

    return answer

print(solution("baby"))