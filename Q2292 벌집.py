n = int(input())

count, pos, step = 1, 1, 6

while n > pos:

    pos += step
    step += 6
    count += 1

print(count)