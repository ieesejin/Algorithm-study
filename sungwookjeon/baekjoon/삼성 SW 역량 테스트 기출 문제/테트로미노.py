def cal_max(new_list):
    result = 0
    for i in range(0, len(new_list)):
        sum_ = 0
        for j in range(0, 4):
            sum_ += map_[new_list[i][j][0]][new_list[i][j][1]]
        result = max(result, sum_)
    return result


def create_list(x_, y_, shape_):
    list1 = []
    for i in range(0, len(shape_)):
        list0 = []
        check = 0
        for j in range(0, 4):
            x = x_ + shape_[i][j][0]
            y = y_ + shape_[i][j][1]
            if x < 0 or y < 0 or x > N - 1 or y > M - 1:
                check = 1
                del list0[:]
                break
            list0.append(list(map(int, (x, y))))
        if check == 1:
            continue
        else:
            list1.append(list0)
    return list1


# stick (2) [2][4][2]
def tetromino_1(x1, y1):
    shape = [
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [2, 0], [3, 0]]
    ]
    list1 = create_list(x1, y1, shape)
    result1 = cal_max(list1)
    return result1


# square (1) [1][4][2]
def tetromino_2(x2, y2):
    shape = [
        [[0, 0], [0, 1], [1, 0], [1, 1]]
    ]
    list2 = create_list(x2, y2, shape)
    result2 = cal_max(list2)
    return result2


# gun (8) [8][4][2]
def tetromino_3(x3, y3):
    shape = [
        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[0, 0], [0, 1], [0, 2], [1, 0]],
        [[0, 0], [0, 1], [1, 1], [2, 1]],
        [[0, 0], [0, 1], [0, 2], [-1, 2]],
        [[0, 0], [1, 0], [2, 0], [2, -1]],
        [[0, 0], [1, 0], [1, 1], [1, 2]],
        [[0, 0], [0, -1], [-1, -1], [-2, -1]],
        [[0, 0], [0, 1], [0, 2], [1, 2]]
    ]
    list3 = create_list(x3, y3, shape)
    result3 = cal_max(list3)
    return result3


# snake (4) [4][4][2]
def tetromino_4(x4, y4):
    shape = [
        [[0, 0], [1, 0], [1, 1], [2, 1]],
        [[0, 0], [0, -1], [1, -1], [1, -2]],
        [[0, 0], [1, 0], [1, -1], [2, -1]],
        [[0, 0], [0, 1], [1, 1], [1, 2]]
    ]
    list4 = create_list(x4, y4, shape)
    result4 = cal_max(list4)
    return result4


# mountain (4) [4][4][2]
def tetromino_5(x5, y5):
    shape = [
        [[0, 0], [0, 1], [0, 2], [1, 1]],
        [[0, 0], [1, -1], [1, 0], [2, 0]],
        [[0, 0], [1, -1], [1, 0], [1, 1]],
        [[0, 0], [1, 0], [1, 1], [2, 0]]
    ]
    list5 = create_list(x5, y5, shape)
    result5 = cal_max(list5)
    return result5


# calculate
def cal(x_, y_):
    return max(tetromino_1(x_, y_), tetromino_2(x_, y_),
               tetromino_3(x_, y_), tetromino_4(x_, y_),
               tetromino_5(x_, y_))


map_ = []
answer = 0
N, M = map(int, input().split())
for i in range(0, N):
    map_.append(list(map(int, input().split())))

for i in range(0, N):
    for j in range(0, M):
        a = cal(i, j)
        answer = max(answer, a)
print(answer)
