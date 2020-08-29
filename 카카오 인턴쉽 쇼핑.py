def solution(gems):
    answer = []

    gemCount = len(set(gems))
    arr = gemCount

    while len(gems) >= arr:
        for i in range(len(gems) - arr + 1):
            if len(set(gems[i : i + arr])) == gemCount:

                return [i + 1, i + arr]
        arr += 1
    return answer

g = ["AA", "AB", "AC", "AA", "AC"]
print(solution(g))