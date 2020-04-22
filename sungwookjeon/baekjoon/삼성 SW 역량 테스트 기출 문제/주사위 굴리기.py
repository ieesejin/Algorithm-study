# 1 -> 1, 3, 4, 6(4, 1, 3, 6) / 1, 2, 5, 6(2, 1, 5, 6)
# 2 -> 2, 3, 4, 5(4, 2, 3, 5) / 1, 2, 5, 6(6, 2, 1, 5)
# 3 -> 1, 3, 4, 6(1, 3, 6, 4) / 2, 3, 4, 5(2, 3, 5, 4)
# 4 -> 1, 3, 4, 6(6, 4, 1, 3) / 2, 3, 4, 5(2, 4, 5, 3)
# 5 -> 2, 3, 4, 5(4, 5, 3, 2) / 1, 2, 5, 6(1, 5, 6, 2)
# 6 -> 1, 3, 4, 6(4, 6, 3, 2) / 1, 2, 5, 6(5, 6, 2, 1)
def dice_move(index_, direction):
    if direction == 1 or direction == 2:
        if direction == 1:
            if index_ == 1 or index_ == 2 or index_ == 5 or index_ == 6:
                index_ = 3
            else:
                if index_ == 3:
                    index_ = 6
                elif index_ == 4:
                    index_ = 1
        if direction == 2:
            if index_ == 1 or index_ == 2 or index_ == 5 or index_ == 6:
                index_ = 4
            else:
                if index_ == 3:
                    index_ = 1
                elif index_ == 4:
                    index_ = 6
    if direction == 3 or direction == 4:
        if direction == 3:
            if index_ == 1 or index_ == 3 or index_ == 4:
                index_ = 2
            else:
                if index_ == 2:
                    index_ = 6
                elif index_ == 5:
                    index_ = 1
                elif index_ == 6:
                    index_ = 5
        if direction == 4:
            if index_ == 1 or index_ == 3 or index_ == 4:
                index_ = 5
            else:
                if index_ == 2:
                    index_ = 1
                elif index_ == 5:
                    index_ = 6
                elif index_ == 6:
                    index_ = 2
    return index_


def print_dice_top_side(index_):
    if index_ == 1:
        return 6
    if index_ == 2:
        return 5
    if index_ == 3:
        return 4
    if index_ == 4:
        return 3
    if index_ == 5:
        return 2
    if index_ == 6:
        return 1


location = 6
dice = [0] * 6
map_ = []
order_ = []
N, M, x, y, K = map(int, input().split())
for i in range(0, N):
    map_.append(list(map(int, input().split())))
order_ = list(map(int, input().split()))

for i in order_:
    tmp = 0
    if i == 1:
        if y == M - 1:
            continue
        y += 1
        tmp = map_[x][y]
        location = dice_move(location, 1)
        top = print_dice_top_side(location)
        print("top:", top)
        print("location:", location)
        if tmp == 0:
            map_[x][y] = dice[location - 1]
        else:
            dice[location - 1] = tmp
            map_[x][y] = 0
        print(dice[top - 1])
    if i == 2:
        if y == 0:
            continue
        y -= 1
        tmp = map_[x][y]
        location = dice_move(location, 2)
        top = print_dice_top_side(location)
        print("top:", top)
        print("location:", location)
        if tmp == 0:
            map_[x][y] = dice[location - 1]
        else:
            dice[location - 1] = map_[x][y]
            map_[x][y] = 0
        print(dice[top - 1])
    if i == 3:
        if x == 0:
            continue
        x -= 1
        tmp = map_[x][y]
        location = dice_move(location, 3)
        top = print_dice_top_side(location)
        print("top:", top)
        print("location:", location)
        if tmp == 0:
            map_[x][y] = dice[location - 1]
        else:
            dice[location - 1] = map_[x][y]
            map_[x][y] = 0
        print(dice[top - 1])
    if i == 4:
        if x == N - 1:
            continue
        x += 1
        tmp = map_[x][y]
        location = dice_move(location, 4)
        top = print_dice_top_side(location)
        print("top:", top)
        print("location:", location)
        if tmp == 0:
            map_[x][y] = dice[location - 1]
        else:
            dice[location - 1] = map_[x][y]
            map_[x][y] = 0
        print(dice[top - 1])
    # print("dice:", dice)
