def solution(answers):
    answer = []
    one, two, three = 0, 0, 0
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    oneCount, twoCount, threeCount = 0, 0, 0

    for i in answers:

        if i == first[oneCount]:
            one += 1
        if i == second[twoCount]:
            two += 1
        if i == third[threeCount]:
            three += 1
        oneCount, twoCount, threeCount = oneCount + 1, twoCount + 1, threeCount + 1

        if oneCount == len(first):
            oneCount = 0
        if twoCount == len(second):
            twoCount = 0
        if threeCount == len(third):
            threeCount = 0

    one, three = 1, 1
    if one == max(one, two, three):
        answer.append(1)
    if two == max(one, two, three):
        answer.append(2)
    if three == max(one, two, three):
        answer.append(3)

    answer.sort()

    return answer

data = [ 1, 2, 5, 2, 1, 3, 1, 5, 3, 1, 5, 4, 4, 2, 3, 1 ]

print(solution(data))

# for i in answers:
#
#     if i == first[oneCount]:
#         one += 1
#     if i == second[twoCount]:
#         two += 1
#     if i == third[threeCount]:
#         three += 1
#     oneCount, twoCount, threeCount = oneCount + 1, twoCount + 1, threeCount + 1
#
#     if oneCount == len(first) - 1:
#         oneCount = 0
#     if twoCount == len(second) - 1:
#         twoCount = 0
#     if threeCount == len(third) - 1:
#         threeCount = 0

