import math

def is_prime_number(n):
    array = [True for i in range(n+1)] 

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array

def isprime(i) :
    if i == 1:
        return False
    elif i == 2 :
        return True
    for n in range(2, int(math.sqrt(i)) + 1) :
        if i%n == 0 :
            return False
    return True


def trans_n(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 


def solution(n, k):
    answer = 0
    # prime_array = is_prime_number(10000000)
    # prime_array[0] = False
    # prime_array[1] = False
    n_num = trans_n(n, k)
    nums = n_num.split("0")
    
    for i in nums:
        if i == '':
            continue
        if isprime(int(i)):
            answer += 1
    return answer

print(solution(437674, 3))