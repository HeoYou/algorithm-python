def solution(n):
    str124 = '412'
    answer = ''
    while n:
        answer = str124[n % 3] + answer
        n = n // 3 - (n % 3 == 0)
    return answer