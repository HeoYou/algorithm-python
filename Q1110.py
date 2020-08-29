
n = int(input())

nlst = []

if n < 10:
    nlst.append(0)
    nlst.append(n)
else:
    nlst.append(n // 10)
    nlst.append(n % 10)
# copylst = copy.deepcopy(nlst)
copylst = nlst[:]
count = 0

while True:
    nlst[0], nlst[1] = nlst[1], (nlst[0] + nlst[1]) % 10
    count += 1

    if nlst == copylst:
        break
print(count)