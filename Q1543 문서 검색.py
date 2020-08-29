s = input()
word = input()

top = 0
count = 0
while top < len(s) - len(word) + 1:
    if s[top:top + len(word)] == word:
        count += 1
        top += len(word)
    else:
        top += 1

print(count)

print(s.count(word))