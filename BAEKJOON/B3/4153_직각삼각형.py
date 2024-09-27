import math

answer = []

while True:
    sides = list(map(int, input().split()))
    if sum(sides) == 0:
        break
    else:
        sides.sort()
        if pow(sides[2], 2) == pow(sides[0], 2) + pow(sides[1], 2):
            answer.append("right")
        else:
            answer.append("wrong")

for i in answer:
    print(i)