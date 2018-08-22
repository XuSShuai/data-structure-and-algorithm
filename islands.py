# 岛问题
# 一个矩阵中只有0和1两种值， 每个位置都可以和自己的上、 下、 左、 右
# 四个位置相连， 如果有一片1连在一起， 这个部分叫做一个岛， 求一个
# 矩阵中有多少个岛？
#
# 举例：
#   0 0 1 0 1 0
#   1 1 1 0 1 0
#   1 0 0 1 0 0
#   0 0 0 0 0 0
#
# 这个矩阵中有三个岛。


def islands(mat):
    height = len(mat)
    width = len(mat[0])
    n_island = 0
    for i in range(height):
        for j in range(width):
            if mat[i][j] == 1:
                explore(mat, i, j, height, width)
                n_island += 1
    return n_island


def explore(mat, i, j, height, width):
    if i < 0 or i > height - 1 or j < 0 or j > width - 1 or mat[i][j] != 1:
        return
    mat[i][j] = 2
    explore(mat, i + 1, j, height, width)
    explore(mat, i - 1, j, height, width)
    explore(mat, i, j + 1, height, width)
    explore(mat, i, j - 1, height, width)


if __name__ == "__main__":
    mat = [[0, 0, 1, 0, 1, 0],
           [1, 1, 1, 0, 1, 0],
           [1, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0]]
    print(islands(mat))

    mat = [[1, 1, 1, 0, 1, 1, 1, 0, 1],
           [0, 1, 0, 0, 0, 0, 0, 0, 1],
           [0, 1, 1, 0, 1, 1, 0, 0, 0],
           [1, 1, 1, 0, 1, 1, 1, 1, 0]]
    print(islands(mat))