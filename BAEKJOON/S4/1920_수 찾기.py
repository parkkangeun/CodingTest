# 2024.10.06
# Python

import sys
input = sys.stdin.readline

def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return '1'
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return '0'

answer = []

n = int(input())
n_list = list(map(int, input().split()))
n_list = merge_sort(n_list)

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    answer.append(binary_search(i, n_list))
    
for i in answer:
    print(i)