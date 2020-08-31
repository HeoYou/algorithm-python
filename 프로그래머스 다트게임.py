def solution(dartResult):
    answer = 0
    score = []
    dr_idx = 0
    dr_idx2 = 0
    for i in range(len(dartResult)):
        
        if dartResult[i] in "SDT":
            score.append(int(dartResult[dr_idx2:i]))
            dr_idx2 = i + 1
            if dartResult[i] == "D":
                score[dr_idx] = score[dr_idx] ** 2
            elif dartResult[i] == "T":
                score[dr_idx] = score[dr_idx] ** 3
            dr_idx += 1

        if dartResult[i] == "*":
            dr_idx2 += 1
            if dr_idx == 1:
                score[0] = score[0] * 2
            else:
                score[dr_idx - 2] = score[dr_idx - 2] * 2
                score[dr_idx - 1] = score[dr_idx - 1] * 2
        elif dartResult[i] == "#":
            dr_idx2 += 1
            score[dr_idx - 1] = score[dr_idx - 1] * -1
        
    answer = sum(score)
    return answer

print(solution("1D2S#10S"))

