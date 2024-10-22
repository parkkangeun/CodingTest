# 2024.10.22
# Python

# n 입력받기
n = int(input())

# n의 값 복사
n_copy = n

cnt = 0
# 계산
while True:
    cnt += 1
    n = (n % 10) * 10 + ((n // 10) + (n % 10)) % 10
    if n == n_copy:
        break

# 출력
print(cnt)