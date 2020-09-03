def solution(p):
    answer = ''
    u = ''
    v = ''
    if len(p) == 0 or chkCorrect(p):
        return p

    for i in range(2, len(p), 2):
        if chkBalance(p[0 : i]):
            u = p[0:i]
            v = p[i:]
            break
    
    if chkCorrect(u):
        answer += u + solution(v)
    else:
        answer += '(' + solution(v) + ')'

        for c in u[1:-1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('

    return answer

def chkBalance(s):

    chk = 0

    for i in s:
        if s == "(":
            chk += 1
        elif s == ")":
            chk -= 1

    return True if chk == 0 else False

def chkCorrect(s):
    if len(s) == 0:
        return True
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        stack.append(s[i])
        if len(stack) >= 2 and stack[-1] == ")" and stack[-2] == "(":
            stack = stack[:-2]
    return True if not stack else False

print(solution(")("))

