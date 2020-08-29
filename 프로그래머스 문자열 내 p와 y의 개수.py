def solution(s):
    pc, yc = 0, 0
    py = "PpYy"
    for i in s:
        if i in py[:2]: pc += 1
        elif i in py[2:]:  yc += 1
    return pc == yc

print(solution("pPoooyY"))