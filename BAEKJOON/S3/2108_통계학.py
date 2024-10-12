# 2024.10.12
# python

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    
    l = h = 0
    merged_arr = []
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
    
    
from sys import stdin

n = int(stdin.readline())

numbers = [int(stdin.readline()) for i in range(n)]
numbers = merge_sort(numbers)
cntSortArr = {}
for i in numbers:
    if i in cntSortArr:
        cntSortArr[i] += 1
    else:
        cntSortArr[i] = 1

print(round(sum(numbers) / len(numbers)))
print(numbers[len(numbers) // 2])
cntSortArr = [k for k, v in cntSortArr.items() if max(cntSortArr.values()) == v]
if len(cntSortArr) == 1:
    print(cntSortArr[0])
else:
    print(cntSortArr[1])
print(abs(numbers[0] - numbers[-1]))