def whole(x_, y_):
    result1 = 0
    result2 = 0
    shape_ = [
        [
            [[0, 0], [0, 1], [0, 2], [0, 3]],
            [[0, 0], [1, 0], [2, 0], [3, 0]]
        ],
        [
            [[0, 0], [0, 1], [1, 0], [1, 1]]
        ],
        [
            [[0, 0], [1, 0], [2, 0], [2, 1]],
            [[0, 0], [0, 1], [0, 2], [1, 0]],
            [[0, 0], [0, 1], [1, 1], [2, 1]],
            [[0, 0], [0, 1], [0, 2], [-1, 2]],
            [[0, 0], [1, 0], [2, 0], [2, -1]],
            [[0, 0], [1, 0], [1, 1], [1, 2]],
            [[0, 0], [0, -1], [-1, -1], [-2, -1]],
            [[0, 0], [0, 1], [0, 2], [1, 2]]
        ],
        [
            [[0, 0], [1, 0], [1, 1], [2, 1]],
            [[0, 0], [0, -1], [1, -1], [1, -2]],
            [[0, 0], [1, 0], [1, -1], [2, -1]],
            [[0, 0], [0, 1], [1, 1], [1, 2]]
        ],
        [
            [[0, 0], [0, 1], [0, 2], [1, 1]],
            [[0, 0], [1, -1], [1, 0], [2, 0]],
            [[0, 0], [1, -1], [1, 0], [1, 1]],
            [[0, 0], [1, 0], [1, 1], [2, 0]]
        ]
    ]

    list1 = []
    for k in range(0, 5):
        length = len(shape_[k])
        for i in range(0, length):
            list0 = []
            check = 0
            for j in range(0, 4):
                x = x_ + shape_[k][i][j][0]
                y = y_ + shape_[k][i][j][1]
                if x < 0 or y < 0 or x > N - 1 or y > M - 1:
                    check = 1
                    del list0[:]
                    break
                list0.append(list(map(int, (x, y))))
            if check == 1:
                continue
            else:
                list1.append(list0)
            result1 = cal_max(list1)
        result2 = max(result2, result1)
    return result2


def cal_max(new_list):
    result = 0
    length = len(new_list)
    for i in range(0, length):
        sum_ = 0
        for j in range(0, 4):
            sum_ += map_[new_list[i][j][0]][new_list[i][j][1]]
        result = max(result, sum_)
    return result


map_ = []
answer = 0
N, M = map(int, input().split())
for i in range(0, N):
    map_.append(list(map(int, input().split())))

for i in range(0, N):
    for j in range(0, M):
        a = whole(i, j)
        answer = max(answer, a)
print(answer)
