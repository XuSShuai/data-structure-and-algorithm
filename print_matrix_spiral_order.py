import numpy as np


def print_matrix_spiral_matrix(mat):
    lx, ly = 0, 0
    rx, ry = mat.shape[0] - 1, mat.shape[1] - 1
    while lx <= rx and ly <= ry:
        one_spiral(mat, lx, ly, rx, ry)
        lx += 1
        ly += 1
        rx -= 1
        ry -= 1


def one_spiral(mat, lx, ly, rx, ry):
    if lx == rx and ly == ry:
        print(mat[lx][ly], end=" ")
    elif lx == rx:
        for i in range(ly, ry + 1):
            print(mat[lx][i], end=" ")
    elif ly == ry:
        for i in range(lx, rx + 1):
            print(mat[i][ly], end=" ")
    else:
        for i in range(ly, ry):
            print(mat[lx][i], end=" ")
        for i in range(lx, rx):
            print(mat[i][ry], end=" ")
        for i in range(ry, ly, -1):
            print(mat[rx][i], end=" ")
        for i in range(rx, lx, -1):
            print(mat[i][ly], end=" ")
    print()


mat = np.arange(3*6).reshape(3, 6)
print(mat)
print_matrix_spiral_matrix(mat)

mat = np.arange(4*6).reshape(4, 6)
print(mat)
print_matrix_spiral_matrix(mat)

mat = np.arange(5*5).reshape(5, 5)
print(mat)
print_matrix_spiral_matrix(mat)

mat = np.arange(6*6).reshape(6, 6)
print(mat)
print_matrix_spiral_matrix(mat)