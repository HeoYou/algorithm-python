data = input().split('-')
answer = sum(map(int, data[0].split('+')))
data.pop(0)
for i in data:
    answer -= sum(map(int, i.split('+')))
print(answer)

