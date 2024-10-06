# 2024.10.06
# Python

n = int(input())

coordinate = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append([x, y])
    
for i in sorted(coordinate, key = lambda x: [x[0], x[1]]):
    print(*i)