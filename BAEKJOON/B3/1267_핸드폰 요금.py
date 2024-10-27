# 2024.10.28
# Python

# 입력 받기
n = int(input())
time = list(map(int, input().split()))

# 통화 시간에 따른 요금 계산
Y = 0
M = 0
for i in time:
    Y += (i // 30 + 1) * 10
    M += (i // 60 + 1) * 15
    
# 출력
if Y == M: print(f'Y M {Y}')
elif Y < M: print(f'Y {Y}')
else: print(f'M {M}')