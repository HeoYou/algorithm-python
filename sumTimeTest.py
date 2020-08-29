import sys
import time

# 10 ** 8 개의 리스트 합계
# sum() 함수 >> time :  2.0719873905181885
# for문 >> time :  8.035916566848755

# 10 ** 9 개의 리스트 합계
# sum() 함수 >> time :  148.41290545463562
# for문 >> time :  79.63932132720947

#갯수가 증가하면 for문이 빨라지게 된다.
dataLst = [i for i in range(10**9)]
sumLst = 0

start = time.time()
print(sum(dataLst))
print("time : ", time.time() - start)

start = time.time()
for i in range(len(dataLst)):
    sumLst += i
print("time : ", time.time() - start)
        