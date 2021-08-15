def solution(servers, sticky, requests):
    dic_lst = [dict() for _ in range(servers)]
    answer = [[] for _ in range(servers)]
    pos = 0
    find = 0
    for i in requests:
        for j in range(servers):
            if dic_lst[j].get(i) != None:
                answer[j].append(i)
                dic_lst[j][i] = 1
                find = 1
                break
        if find == 0:
            dic_lst[pos][i] = 1
            answer[pos].append(i)
            pos = (pos + 1) % servers
            find = 0
        else:
            find = 0
    return answer

print(solution(2, True, [1, 2, 2, 3, 4, 1]))