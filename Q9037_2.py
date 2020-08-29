
def teacher(N, candy):    
    tmp_lst = [0 for i in range(N)]
    
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx + 1) % N] = candy[idx]

    for idx in range(N):
        candy[idx] += tmp_lst[idx]

    return candy

def check(N, candy):
    for idx in range(N):
        if candy[idx] % 2 == 1:
            candy[idx] += 1

    return len(set(candy)) == 1

def process():
    count = 0
    N, candy = int(input()), list(map(int, input().split(" ")))

    while not check(N, candy):
        count += 1
        candy = teacher(N, candy)
    print(count)
    



for i in range(int(input())):
    process()