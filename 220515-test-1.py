import heapq


def solution(v, a, b):
    answer = 0
    
    a_b = a - b
    use = 0
    min_h = []
    max_h = []
    
    for key, val in enumerate(v):
        heapq.heappush(min_h, (val, key))
        heapq.heappush(max_h, (-val, key))
        
    while True:
        if min_h[0][0] <= use + b:
            print(1234)
            break
        if -max_h[0][0] < a:
            break
        
        answer += 1
        v, k = heapq.heappop(max_h)
        v = -v
        min_h.remove((v, k))
        v -= a_b
        use += b
        heapq.heappush(max_h, (-v, k))
        heapq.heappush(min_h, (v, k))
        
    return answer
    


print(solution([4, 4, 3], 2, 1))