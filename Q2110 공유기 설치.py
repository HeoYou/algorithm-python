import sys
N, C = map(int, sys.stdin.readline().split())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
data = sorted(data)
answer = 0

start = data[1] - data[0]
end = data[-1] - data[0]

while start <= end:
    mid = (start + end) // 2
    value = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] >= value + mid:
            value = data[i]
            count += 1
    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)