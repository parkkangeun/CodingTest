# 2024.10.14
# Python

from sys import stdin

n, m = map(int, stdin.readline().split())

pb = {}
for i in range(n):
    pb[i + 1] = stdin.readline().rstrip()
pb_re = {v:k for k, v in pb.items()}

for _ in range(m):
    inpt = stdin.readline().rstrip()
    if  inpt.isdigit():
        print(pb[int(inpt)])
    else:
        print(pb_re[inpt])