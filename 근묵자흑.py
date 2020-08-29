# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

n, k = map(int, input().split(' '))

data = []

data = list(map(int, sys.stdin.readline().split(' ')))

result = (n - k) // (k - 1)
if n <= k:
	print(1);
elif ((n - k) / (k - 1)) % 1 == 0:
	print(result + 1)
else:
	print(result + 2)