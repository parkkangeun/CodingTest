# 2024.11.12
# Python
# DP

from sys import stdin

input = stdin.readline
# 입력
n, m = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

# i번 인덱스 까지의 합
sum_list = [0]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
    sum_list.append(total)

# 출력
for i in range(m):
    num1, num2 = map(int, input().rstrip().split())
    print(sum_list[num2] - sum_list[num1 - 1])