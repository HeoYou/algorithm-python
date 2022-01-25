from copy import deepcopy

answer = [[-1000, []]]

def sum_score(info, score):
    sum_info = 0
    sum_score = 0
    for i in range(len(info)):
        if info[i] < score[i]:
            sum_score += 10 - i
        elif info[i] > score[i]:
            sum_info += 10 - i
    return sum_score - sum_info,  score

def dfs(n, depth, info, score):
    global answer
    ret = [0]
    if sum(score) == n:
        calc_score, final_score = sum_score(info, score)
        if answer[0][0] < calc_score:
            answer = [[calc_score, final_score]]
        elif answer[0][0] == calc_score:
            answer.append([calc_score, final_score])


    for i in range(sum(score), n):
        s = deepcopy(score)
        s[depth] += 1

        print(s, score)
        dfs(n, depth + 1, info, s)


def solution(n, info):

    dfs(n, 0, info, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
