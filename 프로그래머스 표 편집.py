import pprint
def solution(n, k, cmd):
    dic = {i : [i - 1, i + 1, 'O'] for i in range(1, n + 2)}
    pos = k
    undo = []

    for c in cmd:
        if c == 'C':
            undo.append()
            dic[pos][2] = 'X'
            dic[dic[pos][0]][1] = dic[pos][1]
            dic[dic[pos][1]][0] = dic[pos][0]
            if dic[pos][1] > n:
                pos = dic[pos][0]
            else:
                pos = dic[pos][1]

        pprint.pprint(dic)
    answer = ''
    return answer

print(solution(8, 7, ["C", "C", "C"]))




def solution1(n, k, cmd):
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