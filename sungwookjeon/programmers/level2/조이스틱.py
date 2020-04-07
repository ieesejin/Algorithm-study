def solution(name):
    answer = 0
    name = list(name)
    # for i in name:
    #     print(ord(i) - ord('A'), ord('Z') - ord(i))
    # print(9 + (1 + 4) + (1 + 9) + (1 + 12) + (1 + 4) + (1 + 13))
    index_list = list(range(0, len(name)))
    location = ord('A')
    index = 0
    count = 0
    while True:
        mov_min = []
        if count == 0:
            answer += ord(name[index]) - location
            index_list.pop(index)
        else:
            for i in index_list:
                a = ord('Z') - ord(name[i]) + 1
                b = ord(name[i]) - ord('A')
                if a > b:
                    mov_min.append(b)
                else:
                    mov_min.append(a)
            for i in range(0, len(mov_min)):
                if i == len(mov_min) - 1:
                    mov_min[i] += 1
                else:
                    mov_min[i] += (i + 1)
            answer += min(mov_min)
            index = mov_min.index(min(mov_min)) + 1
            answer += ord(name[index]) - location
            index_list.pop(index)
            print(index_list)
        count += 1
        if count == 4:
            break
    return answer
