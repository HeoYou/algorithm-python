import heapq
def solution(arr, processes):
    answer = []
    
    rh = []
    wh = []
    for p in processes:
        p = p.split()
        if p[0] == "read":
            rh.append(list(map(int, p[1:])))
        else:
            wh.append(list(map(int, p[1:])))
        
    print(rh, wh)
    time = min(int(rh[0][0]), int(wh[0][0]))
    
    while rh or wh:
        
        if wh and wh[0][0] <= time:
            time += wh[0][1]
            for i in range(wh[0][2], wh[0][3] + 1):
                arr[i] = wh[0][4]
            wh.pop(0)
            
        elif rh and rh[0][0] <= time:
            time += rh[0][1]
            answer.append("".join(list(map(str, arr[rh[0][2]:rh[0][3] + 1]))))
            rh.pop(0)
        else:
            time += 1
            
        print(arr)
        # print()
        # print()
        # print("time", time)
        # print(arr)
        # print("wh", wh)
        # print("rh", rh)
        # if rh and not wh:
        #     if time < int(rh[0][0]):
        #         print(1)
        #         time = int(rh[0][0]) + int(rh[0][1])
        #         answer.append("".join(list(map(str, arr[int(rh[0][2]):int(rh[0][3]) + 1]))))
        #         rh.pop(0)
        #     else:
        #         print(2)
        #         print(wh, rh)
        #         time += int(rh[0][1])
        #         answer.append("".join(list(map(str, arr[int(rh[0][2]):int(rh[0][3]) + 1]))))
        #         rh.pop(0)
                
        # elif not rh and wh:
        #     if time < wh[0][0]:
        #         print(3)
        #         time = int(wh[0][0]) + int(wh[0][1])
        #         for i in range(int(wh[0][2]), int(wh[0][3])):
        #             arr[i] = wh[0][4]
        #         wh.pop(0)
        #     else:
        #         print(4)
        #         time += int(wh[0][1])
        #         for i in range(int(wh[0][2]), int(wh[0][3])):
        #             arr[i] = wh[0][4]
        #         wh.pop(0)
        # else:
            
        #     if time > int(wh[0][0]):
        #         print(5)
        #         time += int(wh[0][1])
        #         for i in range(int(wh[0][2]), int(wh[0][3])):
        #             arr[i] = wh[0][4]
        #         wh.pop(0)
                
        #     elif time > int(rh[0][0]): 
        #         print(6)
        #         time += int(rh[0][1])
        #         answer.append("".join(list(map(str, arr[int(rh[0][2]):int(rh[0][3]) + 1]))))
        #         rh.pop(0)
                
        #     else:
        #         if int(wh[0][0]) < int(rh[0][0]):
        #             print(7)
        #             time += int(wh[0][1])
        #             for i in range(int(wh[0][2]), int(wh[0][3])):
        #                 arr[i] = wh[0][4]
        #             wh.pop(0)
                        
        #         else: 
        #             print(8)
        #             time += int(rh[0][1])
        #             answer.append("".join(list(map(str, arr[int(rh[0][2]):int(rh[0][3]) + 1]))))
        #             rh.pop(0)
                
        # print(arr)
            
    return answer + [time]

print(solution(["1","2","4","3","3","4","1","5"], ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]))