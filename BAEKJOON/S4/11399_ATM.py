# 2024.10.15
# Pyyhon

from sys import stdin

n = int(stdin.readline().rstrip())
p = sorted(list(map(int, stdin.readline().split())))
answer = 0
for i in range(len(p)):
    answer += sum(p[:i + 1])
print(answer)