# 2024.10.01
# Python

t = int(input())
answer = []
for _ in range(t):
    floor = int(input())
    room = int(input())
    temp = []
    room_list = []
    for i in range(1, room + 1):
        room_list.append(i)
    for i in range(floor):
        temp.clear()
        for ii in range(room):
            temp.append(sum(room_list[:ii + 1]))
        room_list = temp.copy()
    answer.append(room_list)

for i in range(len(answer)):
    print(max(answer[i]))