
def classification(word):
    num, string = '', ''

    for i in word:
        if i in '0123456789':
            num += i
        else:
            string += i
    return num, string



def process(word):
    num, string, answer = '', '', ''

    num, string = classification(word)
    
    if abs(len(num) - len(string)) >= 2:
        return ''

    elif len(num) - len(string) == 1:
        for i in range(len(string)):
            answer += num[i]
            answer += string[i]
        answer += num[-1]

    elif len(num) - len(string) == -1:
        for i in range(len(num)):
            answer += string[i]
            answer += num[i]
        answer += string[-1]    

    else:
        for i in range(len(num)):
            answer += num[i]
            answer += string[i]

    return answer
    
print(process("12f3f4ss4fe"))