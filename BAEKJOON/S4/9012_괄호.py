# 2024.10.08
# Python

n = int(input())
answer = []
for _ in range(n):
    string = input()
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        answer.append('YES')
    else:
        answer.append('NO')
for i in answer:
    print(i)