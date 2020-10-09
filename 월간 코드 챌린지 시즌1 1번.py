
def numeral(number):
    a, b = divmod(number, 3)

    return numeral(a) + str(b) if a else str(b)

def solution(n):
    answer = 0
    n = int(numeral(n)[::-1])

    for idx, val in enumerate(str(n)[::-1]):
        answer += (3 ** idx) * int(val)
    return answer

print(solution(45))

