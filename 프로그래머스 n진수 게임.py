def solution(n, t, m, p):

    answer = ''
    tmp = ''

    i = -1
    while len(answer) != t:
        i += 1
        tmp = tmp + overTen(i, n)
        if len(tmp) >= m:
            answer += tmp[m - p - 1]
            tmp = tmp[m:]

    return answer

def overTen(n,i):
    str1 = ""
    Nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return '0'
    while n != 0:
        if n % i == 0:
            str1 += "0"
        else:
            str1 += str(Nums[n%i])
        n = n // i
    return(str1)[::-1]
        
print(solution(16, 16, 2, 1))
print(overTen(0, 16))