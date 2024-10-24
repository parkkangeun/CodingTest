# 2024.10.24
# Python

from sys import stdin
input = stdin.readline
# 학생 수 받기
num = int(input())
same = [0] * num

# num명의 학생들이 1 ~ 5학년까지 속한 반 받기
std = []
for i in range(num):
    std.append(list(map(int, input().split())))

# 같은 반에 속했던 학생의 유무 
for i in range(num):
    for j in range(i + 1,  num):
        for grade in range(5):
            if std[i][grade] == std[j][grade]:
                same[i] += 1
                same[j] += 1
                break
            
# 최대값을 가진 학생의 인덱스 출력
print(same.index(max(same)) + 1)