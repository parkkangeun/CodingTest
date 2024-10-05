# 2024.10.04
# Python

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

n = str(factorial(int(input())))
cnt = 0
for i in range(len(n) - 1, 0, -1):
    if n[i] == '0':
        cnt += 1
    else:
        break
print(cnt)