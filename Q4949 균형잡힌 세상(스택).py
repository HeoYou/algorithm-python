import sys
cmd = ''
answer = []
while True:
    cmd = input()
    if cmd == '.':
        break
    stack = []
    flag = True

    for s in cmd:

        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif s == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if flag == True and not stack:
        print('yes')
    else:
        print('no')
            

