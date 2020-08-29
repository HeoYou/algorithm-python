a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

def gcd(m,n):
    if n == 0:
        return m
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(m, n)
    else:
        return n



numerator = (a1 * b2) + (a2 * b1)
denominator = a2 * b2

gcdAns = gcd(numerator, denominator)

print(numerator // gcdAns, denominator // gcdAns)


