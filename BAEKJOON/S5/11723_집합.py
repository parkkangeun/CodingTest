# 2024.10.13
# Python

from sys import stdin

m = int(stdin.readline().rstrip())

s = []

for _ in range(m):
    cal = stdin.readline().rstrip()
    if cal == 'all':
        s = [i for i in range(1, 21)]
    elif cal == 'empty':
            s = []
    else:
        cal, num = cal.split()
        num =  int(num)
        if cal == 'add' and num not in s:
            s.append(num)
        elif cal == 'remove' and num in s:
            s.remove(num)
        elif cal == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif cal == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.append(num)