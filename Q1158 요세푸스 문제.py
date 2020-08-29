a, b = map(int, input().split())

lst = [i + 1 for i in range(a)]
answer = []
pos = -1
while lst:
    pos = (pos + b) % len(lst)
    answer.append(lst.pop(pos))
    pos -= 1
print("<" + ', '.join(map(str, answer)) + ">")