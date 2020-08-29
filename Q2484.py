n = int(input())

def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return  lst[0] * 5000 + 50000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]:    #3개의 같은수가 나오고 같은 수 는 다른수보다 작다
            return 10000 + lst[1] * 1000
        else:
            return 2000 + (lst[1] + lst[2]) * 500
    for i in range(3):
        if lst[i] == lst[i + 1]:
            return lst[i] * 100 + 1000
    return lst[3] * 100

print(max(money() for i in range(n)))
        
    