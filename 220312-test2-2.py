def solution(arr):
    
    answer = 0
    arr_dic = {}
    
    for i in arr:
        if arr_dic.get(i):
            arr_dic[i] += 1
        else:
            arr_dic[i] = 1
    
    arr_tmp = sorted([[i, arr_dic[i]] for i in arr_dic], reverse=True)
    
    while True:
        count = 0
        if sum([i[1] for i in arr_tmp]) < 3:
            return answer
        flag = True
        for i in arr_tmp:
            if i[1] >= 2:
                flag = False
        if flag:
            return answer
        
        
        len_arr = len(arr_tmp)
        for i in range(len_arr):
            if arr_tmp[i][1] >= 2:
                arr_tmp[i][1] -= 2
                count += arr_tmp[i][0]
                break
        flag = True
        for i in range(len_arr):
            if arr_tmp[len_arr - i - 1][1] % 2 == 1:
                arr_tmp[len_arr - i - 1][1] -= 1
                count += 1
                flag = False
                break
        if flag:
            for i in range(len_arr):
                if arr_tmp[len_arr - i - 1][1] >= 1:
                    arr_tmp[len_arr - i - 1][1] -= 1
                    count += 1
                
        answer += count    
    
    print(arr_tmp)
    
    return answer


# from re import L


# def solution(arr):
    
#     answer = 0
#     l_arr = sorted(arr, reverse=True)
#     s_arr = sorted(arr)
#     arr_dic = {}
    
#     for i in arr:
#         if arr_dic.get(i):
#             arr_dic[i] += 1
#         else:
#             arr_dic[i] = 1
            
#     print(arr_dic)
    
#     while True:
#         count = 0
#         for l in l_arr:
#             if arr_dic.get(l) and arr_dic.get(l) % 2 == 0:
#                 arr_dic[l] -= 2
#                 l_arr.remove(l)
#                 l_arr.remove(l)
#                 count += l
#                 break
#         for s in s_arr:
#             if arr_dic.get(l) and arr_dic.get(l) % 1 == 0:
#                 arr_dic[s] -= 1
#                 count += 1
#                 break
        
        
    

            
print(solution([2, 2, 3, 3, 8, 8]))