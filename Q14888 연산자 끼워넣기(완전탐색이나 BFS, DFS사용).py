# 모든 연산자가 들어간 경우를 계산해야 하니 BFS를 사용할 것이다.
# 연산자 사용 횟수는 정해져 있으니 그나마 편안

n = int(input())
lst = list(map(int, input().split()))
op = list(map(int, input().split()))
min_v, max_v = 1000000000, -1000000000

def dfs(calc, count, a, s, m, d):
    global min_v, max_v
    # print(calc)
    if count == n:
        min_v = min(calc, min_v)
        max_v = max(calc, max_v)
    
    if a:
        print('a')
        dfs(calc + lst[count], count + 1, a - 1, s, m, d)
    if s:
        print('s')
        dfs(calc - lst[count], count + 1, a, s - 1, m, d)
    if m:
        print('m')
        dfs(calc * lst[count], count + 1, a, s, m - 1, d)
    if d:
        print('d')
        dfs(-(-calc //lst[count]) if calc < 0 else calc // lst[count], count + 1, a, s, m, d - 1) 


dfs(lst[0], 1, op[0], op[1], op[2], op[3])
print(min_v, max_v)