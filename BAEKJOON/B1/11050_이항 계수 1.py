# 2024.10.04
# Python

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

n, k = map(int, input().split())

if k < 0 or n < k:
    print("0")
else:
    print(int(factorial(n) / (factorial(k) * factorial(n - k))))
