import pprint

def solution(goods):
    answer = {g: [] for g in goods}
    dic = {g: dict() for g in goods}
    for c in range(1, max([len(x) for x in goods])):
        for g in goods:
            for i in range(len(g) - c + 1):
                # if not dic[g].get(g[i:i+ c]):
                dic[g][g[i:i+ c]] = True
        
        for g in goods:
            for i in range(len(g) - c + 1):
                word = g[i:i+ c]
                flag = True
                
                for g2 in goods:
                    if g == g2:
                        continue
                    if dic[g2].get(word):
                        flag = False
                    if len(answer[g]) >= 0:
                        continue
                if flag :
                    answer[g].append(word)
    pprint.pprint(answer)
    answer_tmp = [[] for i in range(len(goods))]
    for idx, g in enumerate(goods):
        if answer[g] == []:
            answer_tmp[idx].append("None")
            continue
        lenG = len(answer[g][0])
        for ag in answer[g]:
            if len(ag) > lenG:
                break
            answer_tmp[idx].append(ag)
        
    # answer_tmp = [" ".join(sorted(list(j))) for j in [set(i) for i in answer_tmp]]
        
    return [" ".join(sorted(list(j))) for j in [set(i) for i in answer_tmp]]

# def solution(goods):
#     answer = {g: [] for g in goods}
#     dic = {g: dict() for g in goods}

#     for c in range(1, max([len(x) for x in goods])):
#         for g in goods:
#             for i in range(len(g) - c + 1):
#                 dic[g][g[i:i + c]] = True

#         for g in goods:
#             for i in range(len(g) - c + 1):
#                 word = g[i : i + c]
#                 flag = True

#                 for g2 in goods:
#                     if g == g2:
#                         continue
#                     if dic[g2].get(word):
#                         flag = False
#                     if len(answer[g]) >= 0:
#                         continue

#                 if flag:
#                     answer[g].append(word)
#     answer_tmp = [[] for i in range(len(goods))]

#     for idx, g in enumerate(goods):
#         if answer[g] == []:
#             answer_tmp[idx].append("None")
#             continue

#         lenG = len(answer[g][0])
#         for ag in answer[g]:
#             if len(ag) > lenG:
#                 break
#             answer_tmp[idx].append(ag)


            
#     return [sorted(list(j)) for j in [set(i) for i answer_tmp]]
pprint.pprint(solution(["pencil","cilicon","contrabase","picturelist"]))
pprint.pprint(solution(["abcdeabcd","cdabe","abce","bcdeab"]))



["1","2","4","3","3","4","1","5"]
["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]