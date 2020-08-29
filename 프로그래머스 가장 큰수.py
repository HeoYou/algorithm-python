def solution(numbers):
    
    if sum(numbers) == 0:
        return "0"
    numbers2 = sorted([[idx, i* 4] for idx, i in enumerate(map(str, numbers))], reverse = True, key=lambda x: x[:][1])
    answer = []
    for i in range(len(numbers)):
        answer.append(numbers[numbers2[i][0]])
    return ''.join(map(str, answer))

print(solution([3, 30, 34, 5, 9]))