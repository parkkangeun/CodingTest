def solution(number):
    length = len(number)
    answer = 0
    for i in range(length):
        for ii in range(i + 1, length):
            for iii in range(ii + 1, length):
                if number[i] + number[ii] + number[iii] == 0:
                    answer += 1
    return answer