#  给一个数组arr，和整数aim，可以任意选择arr中的数字， 如果能累加得到
#  aim返回true， 否则返回false。


def get_aim(arr, i, sum, aim):
    if i == len(arr):
        return sum == aim
    return get_aim(arr, i + 1, sum + arr[i], aim) or get_aim(arr, i + 1, sum, aim)


arr = [3, 4, 7, 12, 3]
aim = 9
print(get_aim(arr, 0, 0, aim))