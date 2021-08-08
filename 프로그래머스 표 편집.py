def solution(n, k, cmd):
    lst = ['O' for i in range(n)]
    pos = k
    stack = []
    for c in cmd:
        if c == 'Z':
            undo = stack.pop()
            lst[undo] = 'O'


        elif c == 'C':
            lst[pos] = 'X'
            
            stack.append(pos)
            dir = 1
            while lst[pos] == 'X':
                if pos == n - 1:
                    dir *= -1
                pos += dir

        else:

            vec, move = c.split(' ')
            move = int(move)
            if vec == 'D':
                while move > 0:
                    if pos == n - 1:
                        break

                    if lst[pos + 1] == 'O':
                        move -= 1
                        pos += 1
                    else:
                        pos += 1
            elif vec == 'U':
                while move > 0:
                    # if pos == 0:
                    #     break
                    if lst[pos - 1] == 'O':
                        move -= 1
                        pos -= 1
                    else:
                        pos -= 1


    
    return ''.join(lst)