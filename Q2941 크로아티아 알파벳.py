import sys
input = sys.stdin.readline

str = input().strip()
sum = 0
lenSum = 0
dz = 0

data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in data:
    if i == 'dz=':
        dz = str.count(i)

    sum += str.count(i)
    lenSum += len(i) * str.count(i)

print(len(str) - lenSum + sum + dz)