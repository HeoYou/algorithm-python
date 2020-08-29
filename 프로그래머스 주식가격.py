def solution(prices):
    answer = []
  
    for i in range(len(prices) - 1):
        
        sec = 1
        for j in range(2 + i, len(prices)):
            if prices[i] >= prices[j - 1]:
                break
            else:
                sec += 1
        answer.append(sec)
    answer.append(0)

    return answer

prices = [1, 2, 3, 2, 3]

print(solution(prices))