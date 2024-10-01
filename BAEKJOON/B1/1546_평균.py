# 2024.10.01
# Python
n = int(input())
grade = list(map(int, input().split()))
m = max(grade)
for i in range(len(grade)):
    grade[i] = grade[i] / m * 100
print(sum(grade) / len(grade))