def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for par, com in zip(participant, completion):
        if par != com:
            return par
    return participant[-1]

