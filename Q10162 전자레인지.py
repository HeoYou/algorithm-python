# T = int(input())
# answer = []
# answer.append(T // 300)
# T = T % 300
# answer.append(T // 60)
# T = T % 60
# answer.append(T // 10)
# T = T % 10

# print(-1 if T > 0 else ' '.join(map(str, answer)))
T = int(input())
answer = []
for i in [300, 60, 10]:
    answer.append(T // i)
    T = T % i
print(-1 if T > 0 else ' '.join(map(str, answer)))