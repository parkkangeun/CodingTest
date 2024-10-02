# 2024.10.02
# Python

# sys.stdin.readline 사용
# 계수정렬
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (10000 + 1)

for _ in range(n):
    arr[int(input())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)

# 1 메모리 초과
# print(sorted(numbers))

# 2 메모리 초과
# numbers = []
# for i in range(n):
#     if i == 0:
#         numbers.append(int(input()))
#     else:
#         num = int(input())
#         if num <= numbers[i - 1]:
#             numbers.insert(i - 1, num)
#         else:
#             numbers.append(num)
# print(numbers)

# 3 메모리 초과 (병합 정렬)
# def merge_sort(array):
#     if len(array) < 2:
#         return array
#     mid = len(array) // 2
#     low_arr = merge_sort(array[:mid])
#     high_arr = merge_sort(array[mid:])
#
#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr
# print(merge_sort(numbers))
