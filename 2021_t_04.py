from typing import List


def solution(input):
    answer = []
    lst = input.split('\n')
    m, n = map(int, lst[0].split(' '))
    answer.append(lst[0])

    count = 0
    day = 1

    for cmd in lst[1:]:

        if day % m == 0:
            count = 0

        if cmd == 'NEXT':
            day += 1
            answer.append('-')
        elif cmd == 'SHOW':
            if day < n:
                answer.append('1')
                count += 1
            else:
                answer.append('0')
        elif cmd == 'NEGATIVE':
            count = n
            answer.append('0')
        elif cmd == 'EXIT':
            answer.append('BYE')
            break


    return '\n'.join(answer)

print(solution("2 3\nSHOW\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nEXIT"))