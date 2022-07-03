import sys

input = sys.stdin.readline
n = int(input())

lst = sorted(list(map(int, input().split())))

rlt = 10 ** 10
answer = []
for i in range(n - 2):
    f = lst[i]
    lp = i + 1
    rp = n - 1
    
    while lp < rp:
        sum_v = f + lst[lp] + lst[rp]
        
        if abs(sum_v) <= abs(rlt):
            rlt = sum_v
            answer = [f, lst[lp], lst[rp]]
        
        if sum_v < 0:
            lp += 1
        elif sum_v > 0:
            rp -= 1
        else:
            print(*answer)
            sys.exit()
            
            
print(*answer)