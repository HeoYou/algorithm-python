import heapq

def solution(operations):

    min_q = []
    max_q = []
    
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(min_q, int(i[1:]))
            heapq.heappush(max_q, (-int(i[1:]), int(i[1:])))
            print(min_q)
            print(max_q)
        elif i[0] == 'D':
            if len(min_q) == 0:
                continue
            elif i[2:] == '1':
                heapq.heappop(max_q)
                min_q.pop()
            else:
                heapq.heappop(min_q)
                max_q.pop()
                
    return [0, 0] if len(min_q) == 0 else [max_q[0][1], min_q[0]]


if __name__=='__main__':
    
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))