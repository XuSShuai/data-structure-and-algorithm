#  数组中只有0和1两种值，求包含0和1个数相等的最长子数组的长度
#  将0变为-1， 求长度为0的最长子数组的长度


def longest_length(arr):
    arr = [-1 if x == 0 else 1 for x in arr]
    sum_map_index = dict()
    ac_sum = 0
    max_length = 0
    for i in range(len(arr)):
        ac_sum += arr[i]
        if ac_sum - 0 in sum_map_index.keys():
            max_length = max([max_length, i - sum_map_index[ac_sum - 0]])
        if ac_sum - 0 not in sum_map_index.keys():
            sum_map_index[ac_sum] = i

    return max_length

if __name__ == "__main__":
    arr = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0]
    print(longest_length(arr))