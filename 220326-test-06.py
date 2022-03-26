import heapq

def solution(req_id, req_info):
    answer = []
    account = {id:[0, 0] for id in set(req_id)}
    sale_lst = []
    buy_lst = []
    print(account)
    for idx, v in enumerate(list(zip(req_id, req_info))):
        id = v[0]
        info = v[1]
        print(idx, id, info)
        if info[0] == 0:
            if len(sale_lst) == 0:
                heapq.heappush(buy_lst, [-info[2], idx, info[0], info[1], info[2]])
            else:
                sell = heapq.heappop(sale_lst)
                if sell[4] > info[2]:
                    heapq.heappush(buy_lst, [-info[2], idx, info[0], info[1], info[2]])
                    heapq.heappush(sale_lst, sell)
                else:
                    if sell[3] > info[1]:
                        sell[3] = sell[3] - info[1]
                        account[id][0] += info[1]
                        account[id][1] -= info[2]
                        account[sell[2]][0] -= info[1]
                        account[sell[2]][1] += info[2]
                        heapq.heappush(sale_lst, sell)
                    elif sell[3] == info[1]:
                        account[id][0] += info[1]
                        account[id][1] -= info[2]
                        account[sell[2]][0] -= info[1]
                        account[sell[2]][1] += info[2]
                    else:
                        while info[1] > 0:
                            if 
                        
                        
                        
                    
                    
                    
                    
        else:
            if len(sale_lst) == 0:
                heapq.heappush(sale_lst, [info[2], idx, info[1], info[2]])
            else:
                buy = heapq.heappop(sale_lst)
                if buy
                
    print(123, buy_lst)
            
    return answer

print(solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"], [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]))


# h = []
# for i in range(100):
#     heapq.heappush(h, [50, i])
# for i in range(50):
#     print(heapq.heappop(h))
# heapq.heappush(h, [50, 1])
# for i in range(51):
#     print(heapq.heappop(h))