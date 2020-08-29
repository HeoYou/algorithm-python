# def solution(prices):
#     answer = []
  
#     for i in range(len(prices) - 1):
        
#         sec = 1
#         for j in range(2 + i, len(prices)):
#             if prices[i] >= prices[j - 1]:
#                 break
#             else:
#                 sec += 1
#         answer.append(sec)
#     answer.append(0)

#     return answer

# prices = [1, 2, 3, 2, 3]

# print(solution(prices))


def solution(prices):
    n = len(prices)
    answer = [1] * n
    answer[-1] = 0

    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if prices[i] <= prices[j]:
                answer[i] += 1
            elif prices[i] > prices[j]:
                break


    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))