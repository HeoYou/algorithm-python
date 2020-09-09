def solution(people, limit):
    people.sort()
    answer = 0

    while len(people) > 1:
        answer += 1
        person1 = people.pop()
        maxW = 0
        flag = True

        for i in people:
            if person1 + i > limit:
                flag = False
                break
            maxW = max(maxW, i)
        if flag:
            people.remove(maxW)
    if people:
        return answer + 1

    return answer
print(solution([70, 50, 30, 61, 61, 62, 64], 100))

# def solution(people, limit):
#     answer = 0
    
#     while len(people) > 1:
#         maxW = 0
#         flag = False
#         for i in range(1, len(people)):
#             if people[0] + people[i] <= limit:
#                 maxW = max(maxW, people[i])
#                 flag = True
#         answer += 1
#         if flag:
#             people.pop(0)
#             people.remove(maxW)
#         else:
#             people.pop(0)
#     if people:
#         return answer + 1
#     return answer

# print(solution([70, 50, 80, 50], 100))