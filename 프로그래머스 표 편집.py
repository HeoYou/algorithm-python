import pprint
def solution(n, k, cmd):
    dic = {i : [i - 1, i + 1, 'O'] for i in range(-1, n + 1)}
    pos = k
    undo = []

    for c in cmd:
        if c == 'C':
            undo.append([pos, dic[pos][0], dic[pos][1]])
            dic[pos][2] = 'X'
            dic[dic[pos][0]][1] = dic[pos][1]
            dic[dic[pos][1]][0] = dic[pos][0]
            if dic[pos][1] >= n:
                pos = dic[pos][0]
            else:
                pos = dic[pos][1]
            
        elif c == 'Z':
            num, pre, next = undo.pop()
            dic[num][2] = 'O'
            dic[pre][1] = num
            dic[next][0] = num

        else:
            vec, move = c.split(' ')
            move = int(move)

            if vec == 'D':
                for i in range(move):
                    pos = dic[pos][1]
            elif vec == 'U':
                for i in range(move):
                    pos = dic[pos][0]
        print(c, pos)
        pprint.pprint(dic)

    
    answer = ''

    for i in dic.keys():
        answer += dic[i][2] 
    return answer[1:-1]

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))




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