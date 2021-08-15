def solution(amountText):
    answer = True

    for i in amountText:
        if i not in '0123456789,':
            print(1)
            return False
    
    if amountText[0] == '0' or amountText[0] == ',' or amountText[-1] == ',':
        print(2)
        return False
    
    if ',' in amountText:
        amountText = amountText[::-1]
        for i in range(0, len(amountText)):
            if i % 4 == 3:
                if amountText[i] != ',':
                    return False
            else:
                if amountText[i] not in '0123456789':
                    return False
       
    return True


print(solution(''))