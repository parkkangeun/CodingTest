# 2024.10.13
# python

from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())

lis = deque()
stack = []
num = 1
answer = []
for _ in range(n):
    lis.append(int(stdin.readline().rstrip()))
temp = lis.copy()

while len(lis) != 0:
    if len(stack) == 0 or stack[-1] < lis[0]:
        stack.append(num)
        num += 1
        answer.append('+')
    elif stack[-1] == lis[0]:
        lis.popleft()
        stack.pop()
        answer.append('-')
    else:
        answer.append('NO')
        break
if answer[-1] == 'NO':
    print(answer[-1])
else:
    for i in answer:
        print(i)