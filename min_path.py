#  一个二维数组中的每一个元素都是正数， 要求从左上角走到右下角，
# 每一步只能向右或者是向下， 沿途经过的数字要累加起来，返回最小的路径和。


def min_path(mat, i, j):
    if i == len(mat) - 1 and j == len(mat[0]) - 1:
        return mat[i][j]
    if i == len(mat) - 1:
        return mat[i][j] + min_path(mat, i, j + 1)
    if j == len(mat[0]) - 1:
        return mat[i][j] + min_path(mat, i + 1, j)
    return mat[i][j] + min([min_path(mat, i, j + 1), min_path(mat, i + 1, j)])


if __name__ == "__main__":
    mat = [[1, 3, 2, 0, 2],
           [2, 1, 1, 5, 3],
           [0, 2, 3, 1, 4],
           [0, 0, 1, 1, 3]]
    print(min_path(mat, 0, 0))

    mat = [[1, 3, 5, 9],
           [8, 1, 3, 4],
           [5, 0, 6, 1],
           [8, 8, 4, 0]]
    print(min_path(mat, 0, 0))
