# def solution(fruitWeights, k):
    
#     answer = []
#     for i in range(len(fruitWeights) - k + 1):
#         answer.append(max(fruitWeights[i:i+k]))
    
    
#     return list(sorted(set(answer), reverse=True))

def solution(fruitWeights, k):
    answer = []
    left, right = 0, k 
    m = max(fruitWeights[0:k])
    for i in range(1, len(fruitWeights) - k + 1):
        left, right = left + 1, right + 1
        print(fruitWeights[left:right])

    return answer

print(solution([10, 20, 30, 40, 50], 2))