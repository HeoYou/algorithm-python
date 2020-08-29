def solution(priorities, location):
    answer = 1
    plst = [(idx, i) for idx, i in enumerate(priorities)]

    while True:
        maxPrint = max(priorities)      
        

        if plst[0][0] == location and plst[0][1] == maxPrint:

            break
        elif plst[0][1] == maxPrint:
            priorities.pop(priorities.index(maxPrint))
            plst.pop(0)
            answer += 1
        else:
            plst.append(plst.pop(0))

    
    
    return answer

priorities = [1, 1, 9, 1, 1, 1]

print(solution(priorities, 0))