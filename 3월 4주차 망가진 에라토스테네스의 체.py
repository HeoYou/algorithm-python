# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())

def isPrime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

if n == 1:
    print(0)
else:
    for i in range(2, n // 2 + 1):
        if n // i == 0:
            if isPrime(i) and isPrime(n // i):
                print(1)
            else:
                print(0)
    print(1)
