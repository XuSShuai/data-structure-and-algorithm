# 数组中奇数和偶数个数相等的最长的子数组的长度
# 2 3 3 2 1 4 3 2 2
# 思路：奇数变为1，偶数变为-1，求和为0的最长子数组长度。


def longest_length(arr):
    arr = [-1 if x % 2 == 0 else 1 for x in arr]
    print(arr)
    max_len = 0
    sum_map_index = dict()
    sum_map_index[0] = -1
    ac_sum = 0
    for i in range(len(arr)):
        ac_sum += arr[i]
        if ac_sum in sum_map_index.keys():
            max_len = max([max_len, i - sum_map_index[ac_sum]])
        if ac_sum not in sum_map_index.keys():
            sum_map_index[ac_sum] = i
    return max_len


if __name__ == "__main__":
    arr = [4, 2, 4, 3, 5, 2, 3, 2, 6, 8, 10]
    print(longest_length(arr))

