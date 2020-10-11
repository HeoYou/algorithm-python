# def solution(a):
#     answer = 2
#     mid = a.pop(0)
#     left = []
#     leftMin = 1000000000
#     rightMIn = min(a[1:])

#     for i in range(len(a[1:])):
#         left.append(mid)
#         leftMin = min(leftMin, mid)
#         mid = a.pop(0)
#         # print(rightMIn)
#         if mid == rightMIn:
#             rightMIn = min(a)
#         # print(leftMin, left, mid, a, rightMIn)
#         if mid >= leftMin and mid < rightMIn:
#             answer += 1
#         elif mid < leftMin and mid >= rightMIn:
#             answer += 1
#         elif mid < leftMin and mid < rightMIn:
#             answer += 1


#     return answer



def solution(a):

    leftMin = a[0]
    rightMin = a[-1]
    tmpLst = []
    # print(leftMin, rightMin)
    for i in range(1, len(a) - 1):
        # print(a[i], a[len(a) - i - 1])
        if a[i] < leftMin:
            leftMin = a[i]
            tmpLst.append(i)

        if a[len(a) - i - 1] < rightMin:
            rightMin = a[len(a) - i - 1]
            tmpLst.append(len(a) - i - 1)
    # print(tmpLst)
    return len(set(tmpLst)) + 2

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33, 10]))
print(solution([9, -1, -5]))

# a = []
# b = min(a)