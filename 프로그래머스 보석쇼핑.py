def solution(gems):
    answer = []
    start, end = 0, 0
    gemCount = len(set(gems))

    while len(set(gems[start:end])) != gemCount:
        end += 1
    
    while len(set(gems[start:end])) == gemCount:
        start += 1


    return [start, end]

print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))