# 2024.10.06
# Python

n = int(input())

members = []
for i in range(n):
    age, name = input().split()
    members.append([int(age), name])
members.sort(key=lambda x:x[0])

for i in members:
    print(i[0], i[1])