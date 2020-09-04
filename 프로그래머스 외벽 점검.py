import copy

# def solution(n, weak, dist):
#     answer = 1000

#     weakDist = [0] * len(weak)
#     for i in range(len(weak) - 1):
#         weakDist[i] = weak[i + 1] - weak[i]
#     weakDist[-1] = n - weak[-1] + weak[0]
#     print(weakDist)

#     for i in range(len(weakDist)):
#         print()
#         copyWeakDist = copy.deepcopy(weakDist)
#         weakCount = 0
#         sumCount = 1
#         for _ in range(i):
#             copyWeakDist.append(copyWeakDist.pop(0))
#         for j in range(len(dist) - 1, -1, -1):
#             for x in range(1, len(copyWeakDist)):
#                 print(dist[j], copyWeakDist[:x])
#                 if dist[j] <= sum(copyWeakDist[:x]):
#                     weakCount += 1
#                     copyWeakDist = copyWeakDist[:x]
#                     copyWeakDist.pop()
#                     break
#         answer = min(weakCount, answer)



        
#     return answer

def subRet(lst):
    sum = 0
    for i in range(len(lst) - 1):
        sum += abs(lst[i] - lst[i + 1])
    return 0 if len(lst) == 1 else sum

def solution(n, weak, dist):
    if len(weak) == 1 and len(dist) == 1:
        return 1
    answer = 10000
    dist = sorted(dist, reverse=True)
    weak.append(n + weak[0])

    for _ in range(len(weak)):
        weak.append(weak.pop(0))
        distCount = 0
        copyWeak = copy.deepcopy(weak)
        impo = 1
        # print(copyWeak)
        for i in range(len(dist)):
            # print(dist[i])
            for j in range(len(copyWeak)):
                # print(j, copyWeak[:j], subRet(copyWeak[:j]))
                
                if dist[i] < subRet(copyWeak[:j]):
                    # print(subRet(copyWeak[:j]), 34)
                    distCount += 1
                    copyWeak = copyWeak[j - 1:]
                    # print(copyWeak)
                    break
                if j == len(copyWeak) and len(copyWeak) == 0:
                    impo += 1
        answer = min(answer, distCount)


    if impo == len(weak):
        return -1
    return answer

# print(solution(12, [1,5,6,10],[1,2,3,4]))
# print(solution(12, [1,3,4,9,10],[3,5,7]))
print(solution(200, [0, 100],[1, 1]))
