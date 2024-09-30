# 2024.09.30
# Python

n = int(input())
answer = 1
num = 1
for i in range(n):
    if num < n:
        num += 6 * answer
        answer += 1
    else:
        break
print(answer)