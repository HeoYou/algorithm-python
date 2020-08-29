n = int(input())

def fibo(n):
    if n < 2:
        return n
    
    return fibo(n - 1) + fibo(n - 2)

print(fibo(n))

a = 0
b = 1
for i in range(n):
    a, b = b, a + b
print(a)
