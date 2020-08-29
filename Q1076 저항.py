lst = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
s = ''

for i in range(2):
    data = input()
    s += str(lst.index(data))
data = lst.index(input())
print(int(s) * (10 ** data))
