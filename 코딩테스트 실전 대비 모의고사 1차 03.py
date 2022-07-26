# from collections import deque
# def solution(order):

#     box = deque([i + 1 for i in range(len(order))])
#     chk = deque([0 for i in range(len(order) + 1)])
#     stack = []
#     answer = []

#     for o in order:
#         while True:
#             if box and box[0] == o:
#                 answer.append(o)
#                 box.popleft()
#                 break
#             elif stack and stack[-1] == o:
#                 answer.append(o)
#                 stack.pop()
#                 break
#             else:
#                 if chk[o] == 1:
#                     return len(answer)
#                 else:
#                     b = box.popleft()
#                     chk[b] = 1
#                     stack.append(b)


#     return len(answer)

from collections import deque


def solution(order):
    
    box = deque([i + 1 for i in range(len(order))])
    stack = []
    answer = 0
    
    iCnt = 0
    while box:
        
        if box[0] != order[iCnt]:
            stack.append(box[0])
            
        else:
            iCnt += 1
            answer += 1
            while stack:
                if stack[-1] != order[iCnt]:
                    break
                
                iCnt += 1
                answer += 1
                stack.pop()
        
        box.popleft()
        
    return answer

print(solution([5, 4, 3, 2, 1]))