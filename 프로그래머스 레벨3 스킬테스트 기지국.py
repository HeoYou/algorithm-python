def solution(n, stations, w):
    answer = 0

    lst = [0 for i in range(n + 1)]
    for i in stations:
        lst = lst[:i - w] + [1 for j in range(2 * w + 1)] + lst[i + w:]

    i = 1
    while i <= n:
        if lst[i] == 1:
            i += 1
            continue
        answer += 1
        i += 2 * w + 1


    return answer


n = 16
stations = [9]
w = 2

print(solution(n, stations, w))