# 2024.10.10
# Python
from sys import stdin

def prime_numbers(m, n):
    arr = [i for i in range(m + 1)]
    end = int(m ** (1 / 2))
    for i in range(2, end + 1):
        if arr[i] == 0:
            continue
        for j in range(i * i, m + 1, i):
            arr[j] = 0
    return [i for i in arr[2:] if arr[i] and n <= arr[i]]
m, n = map(int, stdin.readline().split())

answer = prime_numbers(n, m)
for i in answer:
    print(i)