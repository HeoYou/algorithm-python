N, M = map(int, input().split())

lst = list(map(int, input().split()))

myPos = 1
answer = []

for i in range(M):
    
    answer.append(min((lst[i] - myPos) % N, (myPos - lst[i]) % N ))
    myPos = lst[i]

print(' '.join(list(map(str, answer))))

#원형 회전 테이블의 특징은 테이블을 돌릴경우 맨끝의 음식 다음이 처음의 음식이 온다는 점이다.
#이러한 특징을 이용하려면 모듈러를 사용한다.
#음식의 갯수를 모듈러로 나누어주는게 핵심이다.
