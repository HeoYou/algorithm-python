def solution(progresses, speeds):
    answer = []

    while True:
        count = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while True:
            if len(progresses) <= 0:
                break
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break

        if count > 0:
            answer.append(count)
            count == 0

        if len(progresses) <= 0:
            break


    return answer

p = [93,30,55]
s = [3,30,5]

print(solution(p, s))