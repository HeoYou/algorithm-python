stack = []
answer = 0
flag = 0    # 0 = +, 1 = *
for i in input():
    
    if i == '(' or i == '[':
        stack.append(i)
    else:
        if i == ')' and stack[-1] == '[':
            print(0)
            break
        elif i == ']' and stack[-1] == '(':
            print(0)
            break


    

    print(stack)