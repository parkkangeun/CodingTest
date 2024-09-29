# 2024.09.29
# Python

n = int(input())
numbers = list(map(int, input().split()))
answer = 0

for i in numbers:
    for ii in range(2, i + 1):
        if i == ii:
            answer += 1
        elif i % ii == 0:
            break
print(answer)

