# 2024.10.04
# Python

n = int(input())
endNumber = 666
cnt = 0

while True:
    if '666' in str(endNumber):
        cnt += 1
        if cnt == n:
            break
    endNumber += 1
print(endNumber)