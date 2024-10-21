# 2024.10.21
# Python

# n 입력 받기
n = int(input())

# n까지 연산 횟수 저장
d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1 # 1을 뺸다.
    if i % 2 == 0:  # 2로 나누어 떨어질 때, 2로 나누는 연산
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:  # 3으로 나누어 떨어질 떄, 3으로 나누는 연산
        d[i] = min(d[i], d[i // 3] + 1)
        
# 출력
print(d[n])