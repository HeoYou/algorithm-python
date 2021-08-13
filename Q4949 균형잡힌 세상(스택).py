cmd = ''
answer = []
while True:
    cmd = input()
    if cmd == '.':
        break
    stack = []

    for s in cmd:

        if s == '(':
            stack.append('(')
        elif s == '[':
            stack.append('[')
        elif s == ')':
            if len(stack):
                if stack.pop() == '[':
                    print('no')
                    break
            else:
                print('no')
                break

        elif s == ']':
            if len(stack):
                if stack.pop() == '(':
                    print('no')
                    break
            else:
                print('no')
                break
        print(stack)
    if len(stack):
        print('no')
        answer.append('no')
    else:
        print('yes')
        answer.append('yes')

print(answer)

