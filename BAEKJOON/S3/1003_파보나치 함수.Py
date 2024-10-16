# 2024.10.16
# Python

from sys import stdin

# 피보나치 수에서 출력되는 0과 1의 횟수를 구하는 함수
def fibonacci(num):
    if num in memo:
        return memo[num]
    elif num == 0:
        memo[num] = [1, 0]
        return memo[num]
    elif num == 1:
        memo[num] = [0, 1]
        return memo[num]
    else:
        cnt_00 = fibonacci(num - 1)[0] + fibonacci(num - 2)[0]
        cnt_01 = fibonacci(num - 1)[1] + fibonacci(num - 2)[1]
        memo[num] = [cnt_00, cnt_01]
        return memo[num]

# 테스트 케이스 입력
t = int(stdin.readline().rstrip())

# 0과 1이 출력되는 횟수를 t번 출력
for i in range(t):
    num = int(stdin.readline().rstrip())
    memo = {}
    answer = fibonacci(num)
    print(answer[0], answer[1])