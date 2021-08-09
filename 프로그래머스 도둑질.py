def solution(money):
    answer = 0

    if len(money) == 3:
        return max(money)
    
    dp_first = [0] * len(money)
    dp_first[0] = money[0]
    dp_first[1] = money[1]
    dp_first[2] = max(money[0] + money[2], money[1])
    for i in range(3, len(money) - 1):
        dp_first[i] = max(money[i] + dp_first[i - 2], money[i] + dp_first[i - 3])
    print(dp_first)

    dp_last = [0] * len(money)
    dp_last[0] = 0
    dp_last[1] = money[1]
    dp_last[2] = money[2]
    for i in range(3, len(money)):
        dp_last[i] = max(money[i] + dp_last[i - 2], money[i] + dp_last[i - 3])
    print(dp_last)

    return max(max(dp_first[-3:]),max(dp_last[-3:]))

print(solution([1, 100, 3, 1, 5, 3, 100]))
