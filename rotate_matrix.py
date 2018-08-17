import numpy as np


def one_rotate(mat, lx, ly, rx, ry):
    span = rx - lx
    for i in range(span):
        mat[lx][ly + i], mat[lx + i][ry] = mat[lx + i][ry], mat[lx][ly + i]
        mat[lx][ly + i], mat[rx][ry - i] = mat[rx][ry - i], mat[lx][ly + i]
        mat[lx][ly + i], mat[rx - i][ly] = mat[rx - i][ly], mat[lx][ly + i]


def rotate_matrix(mat):
    lx, ly = 0, 0
    rx, ry = mat.shape[0] - 1, mat.shape[1] - 1
    while lx < rx:
        one_rotate(mat, lx, ly, rx, ry)
        lx += 1
        ly += 1
        rx -= 1
        ry -= 1


if __name__ == "__main__":
    mat = np.arange(5 * 5).reshape(5, 5)
    print(mat)
    rotate_matrix(mat)
    print("=" * 50)
    print(mat)

    mat = np.arange(6 * 6).reshape(6, 6)
    print(mat)
    rotate_matrix(mat)
    print("=" * 50)
    print(mat)