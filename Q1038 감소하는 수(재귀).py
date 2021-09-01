from collections import deque
n = int(input())
q = deque([[i] for i in range(10)])
count = 0
if n >= 1023:
   print(-1)
else:
    while True:

        num_lst = q.popleft()
        last_num = num_lst[-1]
        
        for i in range(10):
            if i < last_num:
                q.append(num_lst + [i])
        
        if count == n:
            break
        count += 1
    print(''.join(map(str, num_lst)))