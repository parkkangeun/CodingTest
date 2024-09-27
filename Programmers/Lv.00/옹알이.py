def solution(babbling):
    answer = 0
    for i in babbling:
        i = i.replace("aya", "1")
        i = i.replace("ye", "1")
        i = i.replace("woo", "1")
        i = i.replace("ma", "1")
        i = i.replace("1", "")
        if len(i) == 0:
            answer += 1
    return answer