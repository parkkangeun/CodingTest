# 2024.11.05
# Python

# 변수 선언
virous = [1]
answer = []

# 입력 받기
t = int(input())
n = int(input())

# 그래프 생성
graph = [[] for i in range(t + 1)]
for _ in range(n):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터 찾기
for i in virous:
    for j in graph[i]:
        if j not in virous:
            virous.append(j)
            answer.append(j)

# 출력
print(len(answer))