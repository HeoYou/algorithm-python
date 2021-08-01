def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    answer = new_id

    for i in new_id:
        if i not in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            new_id = new_id.replace(i, '')
    
    for i in range(15, 1, -1):
        if ('.' * i) in new_id:
            new_id = new_id.replace('.' * i, '.')

    if len(new_id) > 0:
        while new_id[:1] == '.':
            new_id = new_id[1:]
    if len(new_id) > 0:
        while new_id[-1:] == '.':
            new_id = new_id[:-1]

    if not new_id:
        new_id = 'a'
    
    new_id = new_id[:15]

    while new_id[-1] == '.':
        new_id = new_id[:-1]

    while len(new_id) <= 2:
        new_id += new_id[-1]

    
    

    answer = new_id
    return answer



print(solution("=.="))
