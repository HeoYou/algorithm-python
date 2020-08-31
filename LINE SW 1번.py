def solution(inputString):
    answer = -1
    start_lst, end_lst = [0 for i in range(4)], [0 for i in range(4)]
    start_pare, end_pare = ['(', '{', '[', '<'], [')', '}', ']', '>']

    for i in range(len(inputString)):

        if inputString[i] in start_pare:
            start_lst[start_pare.index(inputString[i])] += 1
        for j in range(4):
            if start_lst[j] < end_lst[j]:
                return -1
        if inputString[i] in end_pare:
            end_lst[end_pare.index(inputString[i])] += 1   

    if sum(start_lst) == sum(end_lst):
        return sum(start_lst)
    else:
        return -1

data = "line [plus]"
print(solution(data))

