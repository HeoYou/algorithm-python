from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for dungeon in permutations(dungeons):
        count = 0
        copyK = k
        for d in dungeon:
            if copyK >= d[0]:
                copyK -= d[1]
                count += 1
        answer = max(answer, count)
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))