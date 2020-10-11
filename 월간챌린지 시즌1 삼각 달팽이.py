def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    seq = 0
    hei = 0
    wid = 0
    num = 1
    for i in range(n, 0, -1):
        for j in range(i):
            if seq == 0:
                answer[hei][wid] = num
                hei += 1
                
            elif seq == 1:
                wid += 1
                answer[hei][wid] = num

            elif seq ==2:
                hei -= 1
                answer[hei][wid] = num
                wid -= 1
            num += 1
        if seq == 0:
            hei -= 1
        elif seq == 1:
            wid -= 1
        elif seq == 2:
            hei += 1
            wid += 1
        seq += 1
        seq = seq % 3
    answerLst = []
    for i in answer:
        answerLst += i 
        
    return answerLst
print(solution(1000))