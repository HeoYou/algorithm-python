s = input()
lst = 'aeiou'

count = 0
for i in lst:
    count += s.count(i)
print(count)