# 2024.10.06
# Python

n, m = map(int, input().split())
result = []
board = []
for i in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m- 7):
        draw_01 = 0
        draw_02 = 0
        
        for ii in range(i, i + 8):
            for jj in range(j, j + 8):
                if (ii + jj) % 2 == 0:
                    if board[ii][jj] != 'B':
                        draw_01 += 1
                    if board[ii][jj] != 'W':
                        draw_02 += 1
                else:
                    if board[ii][jj] != 'W':
                        draw_01 += 1
                    if board[ii][jj] != 'B':
                        draw_02 += 1
        result.append(draw_01)
        result.append(draw_02)
print(min(result))