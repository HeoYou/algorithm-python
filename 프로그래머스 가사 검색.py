def solution(words, queries):
    answer = []

    for i in queries:
        count = 0
        mid = 0
        if i[0] != '?':
            for j in range(len(i)):
                if i[j] == '?':
                    mid = j
                    print(mid)
                    break
            for j in words:
                if j[:mid] == i[:mid] and len(j) == len(i):
                    count += 1
        else:
            for j in range(len(i)):
                if i[j] != '?':
                    mid = j
                    break
            for j in words:
                if j[mid:] == i[mid:] and len(j) == len(i):
                    count += 1
        answer.append(count)

    return answer


w = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(w, q))