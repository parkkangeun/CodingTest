# 2024.10.08
# Python

from sys import stdin
input = stdin.readline

n = int(input())
basic = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))
dic = {}

for i in basic:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in cards:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')