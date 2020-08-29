def solution(N, stages):
    answer = []
    fail = [0 for i in range(1, N + 1)]
    arr = [0 for i in range(0, N + 1)]

    for i in stages:
        arr[i - 1] +=  1


    for i in range(0, len(arr) - 1):
        fail[i] = arr[i] / len(stages)
        for j in range(arr[i]):
            stages.pop(0)

    tu = [(idx + 1, i) for idx, i in enumerate(fail)]
    for i in range(N):
        for j in range(0, N - i):
            if max(fail) == tu[j - 1][1]:
                fail.pop(j - 1)
                answer.append(tu.pop(j - 1)[0])
    print(fail)


    return answer

N = 5
data = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, data))