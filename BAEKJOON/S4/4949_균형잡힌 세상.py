# 2024.10.08
# Python

answer = []
while True:
    string = input()
    special = []
    if string == '.':
        break
    for i in string:
        if i == '(' or i == '[':
            special.append(i)
        elif i == ']':
            if len(special) != 0 and special[-1] == '[':
                special.pop()
            else:
                special.append(i)
                break
        elif i == ')':
            if len(special) != 0 and special[-1] == '(':
                special.pop()
            else:
                special.append(i)
                break
    if len(special) == 0:
        answer.append('yes')
    else:
        answer.append('no')

for i in answer:
    print(i)