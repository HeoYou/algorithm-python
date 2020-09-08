# def solution(scoville, K):
#     answer = 0
#     while True:
#         if len(scoville) == 1:
#             return -1
#         sum = scoville.pop(0) + scoville.pop(1) * 2
#         scoville.index(1, sum)
#         answer += 1

#         if scoville[0] >= K:
#             break
#         for i in range(1, len(scoville)):
#             if scoville[0] <= scoville[i]:
#                 scoville.index(i, scoville.pop(0))
#     return answer

# print(solution([1, 2, 3, 9, 10, 12], 7))