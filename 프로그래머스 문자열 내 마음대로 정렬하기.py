def solution(strings, n):
    

    answer = sorted(strings)
    return sorted(answer, key=lambda x: x[n])

data = ["abce", "abcd", "cdx"]

print(solution(data, 2))