N, K = map(int, input().split())
data = list(map(int, input()))

stack = []
cnt=0
ans=''
for i in range(N):
    while stack and stack[-1] < data[i] and cnt < K:
        stack.pop()
        K-=1
    stack.append(data[i])

while cnt < K:
    stack.pop()
    K-=1

for i in stack:
    print(i, end='')