# 2024.10.09
# Python


from sys import stdin

n, k = map(int, stdin.readline().split())

circle = [i for i in range(1, n + 1)]
answer = []

d = 0
for _ in range(n):
    d += k - 1
    while len(circle) <= d:
        d = d - len(circle)
    answer.append(str(circle.pop(d)))
        
print('<', ", ".join(answer), '>', sep="")