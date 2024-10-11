# 2024.10.11
# Python

from sys import stdin

input = stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    
    answer = 1
    while imp:
        if imp[0] < max(imp):
            imp.append(imp.pop(0))
        else:
            if m == 0:
                break
            
            imp.pop(0)
            answer += 1
        m = m - 1 if m > 0 else len(imp) - 1
    print(answer)