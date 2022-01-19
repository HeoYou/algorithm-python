def solution(id_list, report, k):
    id_dic = {}
    stop_dic = {}
    answer = [0] * len(id_list)

    for lst in id_list:
        id_dic[lst] = []
        stop_dic[lst] = []
    report = set(report)

    for i in report:
        a, b = i.split()
        id_dic[a].append(b)
        stop_dic[b].append(a)

    for idx, key in enumerate(id_list):
        for id in id_dic[key]:
            if k <= len(stop_dic[id]):
                answer[idx] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
print(solution(id_list, report, 2))