# 2024.10.13
# Python

from sys import stdin

m = int(stdin.readline().rstrip())

s = []

for _ in range(m):
    opr = stdin.readline().rstrip()
    if opr == 'all':
        s = [i for i in range(1, 21)]
    elif opr == 'empty':
            s = []
    else:
        opr, num = opr.split()
        num =  int(num)
        if opr == 'add' and num not in s:
            s.append(num)
        elif opr == 'remove' and num in s:
            s.remove(num)
        elif opr == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif opr == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.append(num)