import copy

def solution(expression):
    answer = []
    sign = []
    seq = ['*-+', '*+-', '+*-', '+-*', '-*+', '-+*']
    def calc(num, pos, s):
        if s == "+":
            num[pos] = num[pos] + num[pos + 1]
            num.pop(pos + 1)
        elif s == '-':
            num[pos] = num[pos] - num[pos + 1]
            num.pop(pos + 1)
        elif s == '*':
            num[pos] = num[pos] * num[pos + 1]
            num.pop(pos + 1)

        return num


    for i in expression:
        if i in '*+-':
            sign.append(i)
    nums = list(map(int, expression.replace('*', '-').replace('+', '-').split('-')))

    for i in seq:
        num2, sign2 = copy.deepcopy(nums), copy.deepcopy(sign)
        for j in i:
            while j in sign2:
                num2 = calc(num2, sign2.index(j), j)
                sign2.pop(sign2.index(j))

        answer.append(abs(num2[0]))
    return max(answer)

print(solution("100-200*300-500+20"))