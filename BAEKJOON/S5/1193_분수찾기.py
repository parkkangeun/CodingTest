# 2024.10.21
# Python

# x 입력받기
x = int(input())
line = 1

# 분수 찾기
while x > line:
    x -= line
    line += 1
    
# 짝수일 경우
if line % 2 == 0:
    a = x
    b = line - x + 1
# 홀수일 경우
else:
    a = line - x + 1
    b = x
    
print(f'{a}/{b}')