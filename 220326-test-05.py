def solution(abilities, k):
    length = len(abilities)
    if length % 2 == 1:
        abilities.append(0)
    
    abilities = sorted(abilities, reverse= True)
    tmp = []
    for i in range(0, length, 2):
        tmp.append([i // 2, abilities[i] - abilities[i + 1]])
    
    tmp = sorted(tmp, key = lambda x:x[1], reverse= True)
    print(tmp)
    
    answer = 0
    for i in tmp[:k]:
        answer += abilities[i[0] * 2]
    for i in tmp[k:]:
        answer += abilities[(i[0] * 2) + 1]
    
    return answer

print(solution([7, 6, 8, 9, 10], 1))