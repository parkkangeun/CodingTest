# 2024.09.30
# Python

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
for i in range(n):
    for ii in range(i + 1, n):
        for iii in range(ii + 1, n):
            num_sum = numbers[i] + numbers[ii] + numbers[iii]
            if num_sum == m or answer < num_sum < m:
                answer = num_sum
    if answer == m:
        break
print(answer)