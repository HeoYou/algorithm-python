def solution(cacheSize, cities):
    answer = 0
    #캐시가 0일경우 바로 반환된다.
    if cacheSize == 0:
        return len(cities * 5)
    lst = [0] * cacheSize
    #대소문자 구별을 인지하지 못한상태로 코딩하였다.
    for city in cities:
        flag = False
        for i in range(cacheSize):
            if lst[i] == city.lower():
                lst.append(lst.pop(i))
                flag = True
                break
        if flag:
            answer += 1
        else:
            lst.pop(0)
            lst.append(city.lower())
            answer += 5
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))