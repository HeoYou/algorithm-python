import sys

print =  sys.stdout.write

count_lst = [0] * 11000

# print(sum(map(int, list(str(55))))
for i in range(10000):
    
    s = i + sum(map(int, list(str(i))))
    count_lst[s] += 1


for idx, v in enumerate(count_lst):
    if idx > 10000:
        break
    if v == 0:
        print(str(idx) + '\n')