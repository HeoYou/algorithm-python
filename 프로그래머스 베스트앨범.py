def solution(genres, plays):
    answer = []
    tmp = {}
    for i in range(len(plays)):
        if genres[i] not in tmp:

            tmp[genres[i]] = [plays[i], [[i, plays[i]]]]

        else:
            tmp[genres[i]][0] += plays[i]
            tmp[genres[i]][1].append([i, plays[i]])

    lst = sorted(list(tmp.values()), reverse = True)
    for i in range(len(lst)):
        lst[i][1] = sorted(lst[i][1], key = lambda x:x[1], reverse = True)
    for i in range(len(lst)):
        for j in range(2):
            if len(lst[i][1]) == 1:
                answer.append(lst[i][1][j][0])
                break
            answer.append(lst[i][1][j][0])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop", "jazz"], [500, 600, 150, 800, 2500, 10000]))

