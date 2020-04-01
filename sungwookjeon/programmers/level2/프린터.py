def solution(priorities, location):
    answer = 0
    # new_list = []
    # for i in enumerate(priorities):
    #     new_list.append(i)
    # index = 0
    # count = 0
    # while True:
    #     if new_list[0][1] < new_list[index][1]:
    #         temp = new_list[0]
    #         new_list.pop(0)
    #         new_list.append(temp)
    #         index = 0
    #         continue
    #     else:
    #         index += 1
    #         if index == len(priorities) - 1:
    #             new_list.pop(0)
    #             count += 1
    #             if new_list[0][0] == location:
    #                 answer = count
    #                 return answer
    max_pr = max(priorities)
    while True:
        temp1 = priorities.pop(0)
        if max_pr == temp1:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_pr = max(priorities)
        else:
            priorities.append(temp1)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer
