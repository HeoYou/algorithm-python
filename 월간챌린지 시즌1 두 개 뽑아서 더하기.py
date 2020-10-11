from itertools import combinations


def solution(numbers):
    answer = []
    comLst = list(combinations(numbers, 2))
    for i in comLst:
        answer.append(sum(i))
    return list(set(sorted(answer)))

print(solution([0, 1]))