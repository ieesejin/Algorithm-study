matrix0 = [[2, 0, 2, 2], [4, 4, 4, 4], [8, 8, 8, 8], [16, 16, 16, 16]]
n = 4
new_list = []
# move right
for i in range(0, n):
    for j in range(0, n - 1):
        tmp0 = j
        if matrix0[i][j] != 0 and matrix0[i][j] == matrix0[i][j+1]:
            tmp1 = matrix0[i][j] + matrix0[i][j+1]
            matrix0[i][j] = tmp1
            matrix0[i][j + 1] = 0
for i in range(0, n):
    for j in range(0, n - 1):
        if matrix0[i][j] == 0:
            num = matrix0[i][j + 1]
            matrix0[i][j] = num
            matrix0[i][j + 1] = 0
        else:
            continue
for i in range(0, n):
    print(matrix0[i])
