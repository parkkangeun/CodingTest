# 2024.10.15
# Python

from sys import stdin

n, k = map(int, stdin.readline().split())
cnt = 0
vl = []
for i in range(n):
    vl.append(int(stdin.readline().rstrip()))

for i in vl[::-1]:
    if k == 0:
        break
    if k // i != 0:
        cnt += k // i
        k = k % i
print(cnt)