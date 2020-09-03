alp = [chr(i+64) for i in range(1, 27)]
count = 27
pos = 0
lengh = 1

def solution(msg):
    answer = []
    while pos >= len(msg):
        flag = False
        for i, a in enumerate(alp):
            if msg(pos) == a:
                answer.append(i + 1)
                flag = True
                pos += len(a)
                lengh = len
                break
        if flag:
            
    return answer

solution(" ")