# 2024.10.05
# Python

import sys
input = sys.stdin.readline

answer = []
people = []
n = int(input())
for _ in range(n):
    people.append(list(map(int, input().split())))

for i in range(len(people)):
    cnt = 1
    for j in range(len(people)):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    answer.append(cnt)
print(*answer)