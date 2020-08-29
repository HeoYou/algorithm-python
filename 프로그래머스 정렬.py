def solution(numbers):

    answer = 0
    numbers.sort()
    numbers.reverse()

    data = [[idx, i] for idx, i in enumerate(numbers)]

    if data[len(data) - 1][0] < data[len(data) - 1][1]:
        return data[len(data) - 1][0] + 1

    for idx, i in data:
        if idx >= i:
            return idx


    return answer

data = [22, 42]

print(solution(data))