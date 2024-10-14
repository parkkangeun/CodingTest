# 2024.10.14
# Python

from sys import stdin

n, m = map(int, stdin.readline().split())
answer = []
dict = {}
for _ in range(n):
    dict[stdin.readline().rstrip()] = 1
for _ in range(m):
    temp = stdin.readline().rstrip()
    if temp in dict:
        dict[temp] += 1
for key in dict:
    if 1 < dict[key]:
        answer.append(key)
print(sorted(answer))