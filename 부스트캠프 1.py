def solution(name):
    answer = True
    flag = True

    for i in range(len(name)):
        for j in range(len(name)):
            if name[i] in name[j] and name.index(name[i]) != name.index(name[j]):
                return True

    return False

name = ["가을", "우주", "너굴"] 

print(solution(name))