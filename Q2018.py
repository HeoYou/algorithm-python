n = int(input())


answer, tot, i= 1, 1, 1

while True:

    i += 1
    tot += i

    if tot > n:
        break
    if (n - tot) % i == 0:
        answer += 1


print(answer)

