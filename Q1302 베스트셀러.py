t = int(input())
book = {}

for i in range(t):
    name = input()
    if name in book.keys():
        book[name] += 1
    else:
        book[name] = 1
book = sorted(book.items(), key=(lambda x : x[0]))
print(max(book, key=lambda x : x[1])[0])