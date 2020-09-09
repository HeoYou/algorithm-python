tc = 1
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    print("Case {}: {}".format(tc, c // b * a + a if c - (b * (c // b)) >= a else c // b * a + (c - (b * (c // b)))))
    tc += 1