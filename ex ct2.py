def process(target, words):
    answer = 0

    for i in words:
        flag = True
        for j in i:
            for k in target:
                if j not in target:
                    flag = False
                    break
        if flag:
            answer += 1
        
    return answer

print(process('abc', ['a','bn','c','ab','ac','bc','ac', 'dd']))
print(process('cloud', ['card','cd','lol','doc']))