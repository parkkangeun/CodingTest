# 2024.11.11
# Python

# 입력받기
t = int(input())


for i in range(t):
    n = int(input())
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 1
        elif i == 3:
            dp[i] = 1
        elif i == 4:
            dp[i] = 2
        elif i == 5:
            dp[i] = 2
        else:
            dp[i] = dp[i - 1] + dp[i - 5]
    print(dp[i])