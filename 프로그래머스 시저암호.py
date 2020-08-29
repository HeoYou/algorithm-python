def solution(s, n):
    answer = []

    for i in s:
        if i != ' ':
            if ord(i) > 95:
                print(1, ord(i) + n)
                if ord(i) + n > 122:
                    print(((ord(i) + n) % 122 + 97))
                
                    answer.append(chr((ord(i) + n) % 122 + 97))
                else:
                    answer.append(chr((ord(i) + n) % 122))
                
            elif ord(i) < 96:
                # print(chr((ord(i) + n) % 90 + 65))
                if ord(i) + n > 90:
                    answer.append(chr((ord(i) + n) % 90 + 65))
                else:
                    answer.append(chr((ord(i) + n) % 90))
            
        else:
            answer.append(" ")
            
    return ''.join(answer)

    

print(ord('a'), ord('z'), ord("A"), ord("Z"))
print(solution("AaZz", 25))