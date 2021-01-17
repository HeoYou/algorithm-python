s, e = map(int, input().split())

#n 까지 수의 소수를 찾기위한 아리토스테네스의 체 함수

def prime_list(n):
    #배열을 만들어준다 True는 소수 False소수가 아니다.
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    #루트 m만큼을 반복하는 이유는 그이상의 수는 나는 아는데 설명하기가 힘들다.
    for i in range(2, m + 1):
        #소수이면 소수의 배수들을 모두 False로 바꿔준다.
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    #0 과 1은 소수가아니다

    sieve[0] = False
    sieve[1] = False
    return sieve

lst = prime_list(e)
for i in range(s, e + 1):
    if lst[i]:
        print(i)