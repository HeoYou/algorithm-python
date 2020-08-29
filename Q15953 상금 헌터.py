n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst += list(map(int, input().split()))

print(' '.join(map(str, sorted(lst))))