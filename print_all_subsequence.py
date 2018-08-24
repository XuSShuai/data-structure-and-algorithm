#  打印一个序列的所有的子序列, 可含空


def print_sub_sequence(string, i, res):
    if i == len(string):
        print(res)
        return
    print_sub_sequence(string, i + 1, res)
    print_sub_sequence(string, i + 1, res + string[i])


if __name__ == "__main__":
    print_sub_sequence("abc", 0, " ")