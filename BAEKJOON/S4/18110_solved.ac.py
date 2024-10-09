# 2024.10.09
# Pyyhon

from sys import stdin

def merge_sort(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    low_array = merge_sort(array[:mid])
    high_array = merge_sort(array[mid:])
    
    merge_arr = []
    l = h = 0
    while l < len(low_array) and h < len(high_array):
        if low_array[l] < high_array[h]:
            merge_arr.append(low_array[l])
            l += 1
        elif high_array[h] <= low_array[l]:
            merge_arr.append(high_array[h])
            h += 1
    merge_arr += low_array[l:]
    merge_arr += high_array[h:]
    
    return merge_arr

def round(val):
    if 0.5 <= val - int(val):
        return int(val) + 1
    else:
        return int(val)

n = int(stdin.readline())
if n:
    opn= []

    for _ in range(n):
        num = int(stdin.readline())
        opn.append(num)

    opn = merge_sort(opn)
    ratio = round(n * 0.15)
    if ratio > 0:
        opn = opn[ratio : - ratio]

    print(round(sum(opn) / len(opn)))
else:
    print(0)