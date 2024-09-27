def solution(k, score):
    answer = []
    temp = []
    for i in score:
        temp.append(i)
        temp.sort(reverse=True)
        if k < len(temp):
            del temp[-1]
        answer.append(min(temp))
    return answer