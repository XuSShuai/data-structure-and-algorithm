# 给定一个数组， 求如果排序之后， 相邻两数的最大差值， 要求时
# 间复杂度O(N)， 且要求不能用非基于比较的排序。


def max_gap(arr):
    min_num = min(arr)
    max_num = max(arr)

    has_num = [0] * (len(arr) + 1)
    min_list = [max_num] * (len(arr) + 1)
    max_list = [min_num] * (len(arr) + 1)

    for num in arr:
        id = int((num - min_num) // ((max_num + 1 - min_num) / (len(arr) + 1)))
        has_num[id] = 1
        min_list[id] = num if min_list[id] > num else min_list[id]
        max_list[id] = num if max_list[id] < num else max_list[id]

    result = 0
    large = max_list[0]
    for i in range(1, len(arr) + 1):
        if has_num[i] == 1:
            result = max([result, min_list[i] - large])
            large = max_list[i]

    return result


arr = [1, -21, 3, 6, 111]
res = max_gap(arr)
print(res)