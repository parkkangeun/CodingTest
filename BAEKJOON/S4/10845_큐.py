# 2024.10.09
# Python

from sys import stdin

n = int(stdin.readline())
q = []

for _ in range(n):
    order = stdin.readline().split()
    if len(order) == 2:
        q.append(int(order[1]))
    elif order[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(q) == 0:
            print(-1)
        elif order[0] == 'front':
            print(q[0])
        else:
            print(q[len(q) - 1])