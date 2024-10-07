# 2024.10.07
# Python

from collections import deque

n = int(input())

deque = deque([i for i in range(1, n + 1)])
while len(deque) > 1:
    deque.popleft()
    temp = deque.popleft()
    deque.append(temp)
print(deque[0])

# import queue
# n = int(input())
# que = queue.Queue()
# for i in range(1, n + 1):
#     que.put(i)
# while True:
#     que.get()
#     if que.qsize() == 1:
#         break
#     que.put(que.get())
# print(que.get())

# cards = [i for i in range(1, int(input()) + 1)]

# while True:
#     cards.pop(0)
#     if len(cards) == 1:
#         break
#     cards.append(cards[0])
#     cards.pop(0)
# print(*cards)