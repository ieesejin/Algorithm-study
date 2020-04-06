# failed
def solution(arrangement):
    answer = 0
    num = 0
    check = 0
    for i in arrangement:
        if i == '(':
            num += 1
            check = 0
        else:
            if check == 0:
                num -= 1
                check = 1
    return answer
