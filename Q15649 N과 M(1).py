N, M = map(int, input().split())

visit = [0] * N
out = []
print(range(N))

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, out)))
        return
