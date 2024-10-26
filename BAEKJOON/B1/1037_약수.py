# 2024.10.26
# Python

# 입력 받기
n = int(input())
a = list(map(int, input().split()))
a.sort()

# N 구하기
answer = a[0] * a[-1]

# 출력
print(answer)