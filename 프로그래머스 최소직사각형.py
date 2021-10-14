def solution(sizes):
    answer = 0
    maxmax, minmax = 0, 0
    for card in sizes:
        maxmax = max(max(card), maxmax)
        minmax = max(min(card), minmax)

    
    return maxmax * minmax

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))