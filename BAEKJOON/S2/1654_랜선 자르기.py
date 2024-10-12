# 2024.10.13
# Python

from sys import stdin

k, n = map(int, stdin.readline().split())
lis = []
for _ in range(k):
    lis.append(int(stdin.readline().rstrip()))

low = 1
high = max(lis)

while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for i in lis:
        cnt += i // mid
    if cnt >= n:
        low = mid + 1
    else:
        high = mid - 1
print(high)