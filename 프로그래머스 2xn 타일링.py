def solution(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b % 1000000007


print(solution(52) % 1000000007)

def solution(n):
    lst = [0] * (n + 1)
    lst[1], lst[2] = 1, 2

    for i in range(3, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    answer = lst[n]
    return answer % 1000000007
print(solution(5))