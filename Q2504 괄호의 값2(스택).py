
stack = []
answer = [0] * 35
flag = 0
pos = 0

for s in input():

    if s == '(' or s == '[':
        stack.append(s)
        flag = 0
        pos += 1

    
    else:
        if s == ')' and stack[-1] == '[':
            print(0)
        elif s == ']' and stack[-1] == '(':
            print(0)
        elif s == ')':
            if flag == 0:
                answer[pos] += 2
                flag = 1
            else:
                answer[pos] *= 2
        elif s == ']':
            if flag == 0:
                answer[pos] += 3
                flag = 1
            else:
                answer[pos] *= 3
    print(answer)
print(sum(answer))
