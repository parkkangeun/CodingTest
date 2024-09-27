def solution(k, score):
    answer = []
    temp = []
    for i in score:
        if len(temp) < k:
            temp.append(i)
        else:
            temp.sort()
            if temp[0] < i:
                del temp[0]
                temp.append(i)
        answer.append(min(temp))
    return answer