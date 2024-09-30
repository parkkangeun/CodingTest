# 2024.09.29
# Python

n = int(input())
size = list(map(int, input().split()))
bundles = list(map(int, input().split()))
answer = 0

for i in size:
    if i % bundles[0] == 0:
        answer += i // bundles[0]
    else:
        answer += (i // bundles[0]) + 1

print(answer)
print(n // bundles[1], n % bundles[1])