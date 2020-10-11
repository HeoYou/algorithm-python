def solution(arr):
    answer = 1
    arr = sorted(arr, reverse = True)
    while True:
        flag = True
        for i in arr:
            if answer % i != 0:
                flag = False
                break
        if flag:
            return answer
        answer += 1

    return answer

print(solution([2,6,8,14]))