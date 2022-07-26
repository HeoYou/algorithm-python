def solution(want, number, discount):
    answer = 0
    
    wantDic = {}
    disDic = {}
    
    for w, n in zip(want, number):
        wantDic[w] = n
        disDic[w] = 0
    
    for idx, item in enumerate(discount):
        idx = idx + 1
        if idx < 11:
            if disDic.get(item):
                disDic[item] += 1
            else:
                disDic[item] = 1
        else:
            if disDic.get(item):
                disDic[item] += 1
            else:
                disDic[item] = 1
            
            disDic[discount[idx- 11]] -= 1     
        
        print(disDic)    
        
        if chk(wantDic, disDic):
            answer += 1
        
    return answer



def chk(w, d):
    for i in w:
        if w[i] != d[i]:
            return False
    return True 
        
print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], 
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
