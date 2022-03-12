def solution(money, costs):
    answer = 0
    coin_lst = [1, 5, 10, 50, 100, 500]
    e_lst = []
    for i in range(6):
        e_lst.append([coin_lst[i], costs[i],  costs[i] / coin_lst[i]])
        
    e_lst = sorted(e_lst, key = lambda x: x[2])
    
    for c, p, _ in e_lst:
        count_coin = money // c
        answer += count_coin * p
        money = money % c
        
    
    return answer

print(solution(1999, [2, 11, 20, 100, 200, 600]))
