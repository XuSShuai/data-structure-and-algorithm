import numpy as np


def zig_zag_print(mat):
    first_x = 0
    first_y = 0
    second_x = 0
    second_y = 0
    from_up = False
    row, col = mat.shape[0] - 1, mat.shape[1] - 1
    while first_x <= row:
        print_diagonal(mat, first_x, first_y, second_x, second_y, from_up)
        from_up = not from_up
        first_x = first_x + 1 if first_y == col else 0
        first_y = col if first_y == col else first_y + 1
        second_y = second_y + 1 if second_x == row else 0
        second_x = row if second_x == row else second_x + 1
    print()


def print_diagonal(mat, first_x, first_y, second_x, second_y, from_up):
    if from_up:
        for i, x in enumerate(range(first_x, second_x + 1)):
            print(mat[x][first_y - i], end=" ")
    else:
        for i, x in enumerate(range(second_x, first_x - 1, -1)):
            print(mat[x][second_y + i], end=" ")


mat = np.arange(4*5).reshape(4, 5)
print(mat)
zig_zag_print(mat)

mat = np.arange(2*5).reshape(2, 5)
print(mat)
zig_zag_print(mat)