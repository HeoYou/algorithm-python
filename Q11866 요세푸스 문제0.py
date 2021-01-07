k, n = map(int, input().split())
pos = n - 1
answer = []
que = [i for i in range(1, k + 1)]

for i in range(k - 1):
    answer.append(que.pop(pos))
    pos = (pos + n - 1) % len(que)
answer += que

print('<', ', '.join(map(str, answer)), '>', sep='')