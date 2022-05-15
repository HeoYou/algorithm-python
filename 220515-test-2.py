import pprint
def solution(logs):
    dic = {}
    
    answer = []
    for i in logs:
        s, num, score = i.split()
        if dic.get(s):
            dic[s][num] = score
        else:
            dic[s] = {num : score}
    
    for k in dic:
        if len(dic[k]) >= 4:
            for k2 in dic:
                if k == k2 or len(dic[k2]) < 5:
                    continue
                if dic[k] == dic[k2]:
                    answer.extend([k, k2])
            
    return sorted(list(set(answer))) if answer else ["None"]

print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]))