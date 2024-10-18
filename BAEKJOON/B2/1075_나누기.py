# 2024.10.18
# Python

# n 과 f 입력받기
n = input()
f = int(input())

# 나누기
n = int(n[:len(n) - 2] + '00')
while n % f != 0:
    n += 1
    
# 출력
n = str(n)
print(n[len(n) - 2:])