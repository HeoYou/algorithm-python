n = int(input())
answer = 0
result = 1
for i in range(n, 0, -1):
    result *= i
strResult = str(result)

for i in range(len(strResult) - 1, -1, -1):
    if strResult[i] == '0':
        answer += 1
    else:
        break
print(answer)