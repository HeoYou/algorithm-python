def solution(infos, queries):
    answer = [0] * len(queries)

    count = -1

    for query in queries:
        count += 1

        query = query.split()
        for info in infos:
            info = info.split()
            if query[0] != '-':
                if query[0] != info[0]:
                    continue
                pass
            if query[0] != '-':
                if query[2] != info[1]:
                    continue
                pass
            if query[0] != '-':
                if query[4] != info[2]:
                    continue
                pass
            if query[0] != '-':
                if query[6] != info[3]:
                    continue
                pass
            if query[7] >= info[4]:
                continue
            answer[count] += 1

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]



print(solution(info, query))