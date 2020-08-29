def solution(str1, str2):
    # 영어가 아닌부분을 제외해야 하기 때문에 apped로 대체
    # lst1, lst2 = [0] * (len(str1) - 1), [0] * (len(str2) - 1) 
    lst1, lst2 = [], []
    str1 = str1.upper()
    str2 = str2.upper()
    print(str1, str2) #테스트
    # print(str1[1])
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            lst1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            lst2.append(str2[i:i + 2])
      
        # append로 수정과정중에 삭제
        # lst2[i] = str2[i:i + 2].upper()
    # 방법을 바꿔서 삭제
    # lst1.sort()
    # lst2.sort()
    intersection = 0

    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                lst2.pop(j)
                intersection += 1
                break

    # print(intersection) 테스트

    
    answer = int(intersection / len(lst1 + lst2) * 65536) if len(lst1 + lst2) > 0 else 65536
    return answer

print(solution("E=M*C^2", "e=m*c^2"))