# 2024.10.01
# Python
answer = []
while True:
    num = input()
    if num == '0':
        break
    else:
        if num == num[::-1]:
            answer.append('yes')
        else:
            answer.append('no')
for i in answer:
    print(i)