# 2024.10.17
# Python

from sys import stdin

a, b = stdin.readline().split()

a, b = int(a[::-1]), int(b[::-1])

if b < a:
    print(a)
else:
    print(b)