# 2024.10.15
# Python

from sys import stdin

n, m = map(int, stdin.readline().split())
dict = {}
for i in range(n):
    addr, pw = stdin.readline().split()
    dict[addr] = pw
for _ in range(m):
    print(dict[stdin.readline().rstrip()])