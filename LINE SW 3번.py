
def solution(road, n):

    road_lst = list(map(int, road))
    
    result_lst = []
    road_point_lst = [0]
    count = 0
    while True:
        count = 0
        start_point, end_point = 0, 0
        for i in range(road_point_lst[-1], len(road_lst)):

            if count == 0:
                road_point_lst.append(i + 1)
            if road_lst[i] == 0:
                road_lst[i] = 1
                count += 1
            if count == n:
                break

        for i in range(len(road_lst)):
            if road_lst[i] == 0:
                end_point = i
                result_lst.append(end_point - start_point)
                start_point = i + 1
        if count < n:
            break
        road_lst = list(map(int, road))
    if len(result_lst) == 0:
        return len(road_lst)
    else:
        return max(result_lst)

data = "111011110011111011111100011111"
print(solution(data, 3))

