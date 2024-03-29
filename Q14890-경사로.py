import sys
input = sys.stdin.readline

def chk(line):
    for i in range(1, N):
        if abs(line[i] - line[i - 1]) > 1:
            return False
        if line[i] < line[i - 1]:
            for j in range(L):
                if i + j >= N or line[i] != line[i + j] or slope[i + j]:
                    return False
                if line[i] == line[i + j]:
                    slope[i + j] = True
        elif line[i] > line[i - 1]:
            for j in range(L):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or slope[i - j - 1]:
                    return False
                if line[i - 1] == line[i - j - 1]:
                    slope[i - j - 1] = True
    return True
		
		

N, L = map(int, input().split())

b = [list(map(int, input().split())) for i in range(N)]
answer = 0

for i in range(N):
    slope = [False] * N
    if chk([b[i][j] for j in range(N)]):
        answer += 1

for j in range(N):
    slope = [False] * N
    if chk([b[i][j] for i in range(N)]):
        answer += 1

print(answer)