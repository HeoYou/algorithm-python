a = 'aeiou'
while True:
    count = 0
    s = input().lower()
    if s == '#':
        break
    for i in a:
        count += s.count(i)
    print(count)