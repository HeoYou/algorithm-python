# from itertools import combinations

def process(arr):
    answer = 0

    # for i in range(1, len(arr), 2):
    #     lst = list(combinations(arr, i))
    #     answer += sum([sum(i) for i in lst])

    for i in range(1, len(arr) + 1, 2):
        for j in range(len(arr) - i + 1):
            answer += sum(arr[j : j+i])

    return answer

print(process([1, 4, 2, 5, 3]))


