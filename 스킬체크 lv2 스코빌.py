import heapq

def solution(scoville, K):

    answer = 0
    heapq.heapify(scoville)

    while scoville:
        if scoville[0] >= K:
            return answer
        if len(scoville) == 1 and scoville[0] < K:
            reutrn -1
        
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer

print(solution([4, 1, 2, 5, 3, 9, 10, 12], 6))