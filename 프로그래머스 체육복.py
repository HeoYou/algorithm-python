def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in range(n):

        if i + 1 in reserve and i + 1 in lost:
            reserve.remove(i + 1)
            lost.remove(i + 1)
            answer += 1

    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            answer += 1
            continue
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            answer += 1

    return answer



print(solution(	10, [3, 9, 10], [3, 8, 9]))








# def solution(n, lost, reserve):

#     count = 0 

#     lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
#     count1, count2 = 0, 0
#     reserve2 = reserve[:]
#     for i in range(len(lost)):
#         for j in range(len(reserve)):
#             if lost[i] - reserve[j] == 1:
#                 count1 += 1
#                 reserve.pop(j)

#                 break 
#     if count1 < len(lost):
#         for i in range(len(lost)):
#             for j in range(len(reserve)):
#                 if lost[i] - reserve[j] == -1:
#                     count1 += 1
#                     reserve.pop(j)
#                     break 

#     for i in range(len(lost)):
#         for j in range(len(reserve2)):
#             if lost[i] - reserve2[j] == 1:
#                 count2 += 1
#                 reserve2.pop(j)

#                 break 
#     if count2 < len(lost):
#         for i in range(len(lost)):
#             for j in range(len(reserve2)):
#                 if lost[i] - reserve2[j] == -1:
#                     count2 += 1
#                     reserve2.pop(j)
#                     break 
    
#     return n - len(lost) + max(count1, count2)