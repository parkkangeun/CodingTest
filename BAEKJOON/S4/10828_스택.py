# 2024.10.09
# Python

from sys import stdin
stack = []
n = int(stdin.readline())

for _ in range(n):
    order = stdin.readline().split()
    if len(order) == 2:
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])