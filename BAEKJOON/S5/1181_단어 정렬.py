# 2024.10.04
# Python

n = int(input())
word = []
for _ in range(n):
    temp = input()
    if temp not in word:
        word.append(temp)
word.sort()
word.sort(key=len)
for i in word:
    print(i)

# 런타임 에러
# word_list = [[] for _ in range(51)]
# n = int(input())
#
# for _ in range(n):
#     word = input()
#     if word not in word_list[len(word)]:
#         word_list[len(word)].append(word)
#
# word_list = list(filter(None, word_list))
#
# for i in word_list:
#     i.sort()
#     for ii in i:
#         print(ii)