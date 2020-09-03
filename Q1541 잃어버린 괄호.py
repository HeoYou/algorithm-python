data = input().split('-')
answer = sum(list(map(int, data[0].split('+'))))
data.pop(0)
for i in data:
    answer -= sum(list(map(int, i.split('+'))))
print(answer)

