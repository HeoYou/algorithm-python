import heapq
def solution(n, works):
    h = []
    for i in works:
        heapq.heappush(h, -i)
    for i in range(n):
        heapq.heappush(h, heapq.heappop(h) + 1)
    answer = 0
    for i in range(len(works)):
        num = heapq.heappop(h)
        if num <= 0:
            answer += num ** 2
    return answer

print(solution(4, [4, 3, 3]))