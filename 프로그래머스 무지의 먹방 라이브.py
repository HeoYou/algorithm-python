def solution(food_times, k):
    answer = 1
    ft = sorted([[food_times[i], i + 1] for i in range(len(food_times))], key = lambda x:x[0])

    lenFood = len(food_times)
    foodIdx, foodTimes = 0, 0
    tmpFood = 0
    while lenFood <= k:
        if lenFood == 0 and k >= 0:
            return -1
        if tmpFood == ft[foodIdx]:
            k -= 1
        else:
            k -= (ft[foodIdx][0] - tmpFood) * lenFood    
        lenFood -= 1
        tmpFood = ft[foodIdx][0]
        foodIdx += 1
        # print(lenFood, k)

    
    ft = sorted(ft[foodIdx:], key = lambda x:x[1])


    return ft[k][1]

print(solution([1, 1, 1, 1], 4)) # 3