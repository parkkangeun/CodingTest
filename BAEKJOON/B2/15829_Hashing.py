# 2024.10.01
# Python

r = 31
m = 1234567891

string_len = int(input())
string = input()
answer = 0
for i in range(string_len):
    answer += (ord(string[i]) - 96) * r ** i
print(answer % m)