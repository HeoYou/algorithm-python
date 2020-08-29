def solution(s):
    num = "0123456789"
    lenS = "46"
    if str(len(s)) not in lenS:
        return False
    for i in s:
        if i not in num:
            print(12)
            return False
    return True

print(solution("1234"))