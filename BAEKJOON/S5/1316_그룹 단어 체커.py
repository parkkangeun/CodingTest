# 2024.10.25
# Python

# 단어의 개수 n 입력받기
n = int(input())

# n개의 단어 입력받기
group = []
for _ in range(n):
    group.append(input())
    
# 그룹 단어 찾기
for word in group:
    temp = []
    for index, value in enumerate(word):
        if value not in temp:
            temp.append(value)
        elif value != word[index - 1]:
            n -= 1
            break

# 출력
print(n)