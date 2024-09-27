def solution(a, b, n):
    answer = 0
    temp = 0
    while a <= n:
        temp = n % a 
        n = (n // a) * b
        answer += n
        n += temp
    return answer


print(solution(2, 1, 20)) 