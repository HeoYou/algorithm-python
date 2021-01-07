def process(arr):
    answer = 0
    arrLen = len(arr)
    for i in range(arrLen):
        answer += arr[i][i]
        answer += arr[arrLen - i - 1][i]

    if len(arr) % 2 == 1:
        answer -= arr[arrLen // 2][arrLen // 2]
    
    return answer

print(process([[1, 1, 1, 2], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 2]]))
print(process([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))