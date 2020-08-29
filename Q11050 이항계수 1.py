N, K = map(int, input().split())

def fatorial(n):
    if n <= 1:
        return 1
    sum = 1
    while n != 1:
        sum *= n
        n -= 1
    return sum

print(fatorial(N)//(fatorial(K)*fatorial(N - K)))


# n,k=map(int, input().split())
# a = 1
# b = 1
# while k:
#     a*=n
#     b*=k
#     n-=1
#     k-=1
# print(a//b)