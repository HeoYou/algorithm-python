def solution(weights, head2head):
    answer = []
    winRate = [[i, weights[i - 1], 0, 0, 0, .0] for i in range(1, len(weights) + 1)]

    for i in range(len(head2head)):
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W':
                winRate[i][2] += 1
                winRate[i][3] += 1
                if weights[i] < weights[j]:
                    winRate[i][4] += 1
            elif head2head[i][j] == 'L':
                winRate[i][2] += 1
    for i in range(len(winRate)):
        if winRate[i][2] != 0:
            winRate[i][5] = winRate[i][3] / winRate[i][2]

    winRate = sorted(winRate, key = lambda x:x[1], reverse =True)
    winRate = sorted(winRate, key = lambda x:x[4], reverse =True)
    winRate = sorted(winRate, key = lambda x:x[5], reverse =True)

    # print(winRate)

    for win in winRate:
        answer.append(win[0])
    return answer

print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))