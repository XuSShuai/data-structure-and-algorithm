# 给定一个数组arr和一个整数num,求在arr中累加和等于num的最长子数组的长度
# 例子:
# arr = {7,3,2,1,1,7,7,7} num = 7
# 其中有很多的子数组累加和等于7， 但是最长的子数组是{3,2,1,1}， 所以返回其长度4


def longest_length(arr, aim):
    sub_sum = dict()
    sub_sum[0] = -1
    ac_sum = 0
    length = 0
    for i in range(len(arr)):
        ac_sum += arr[i]
        if ac_sum - aim in sub_sum.keys():
            length = max([length, i - sub_sum[ac_sum - aim]])
        if ac_sum not in sub_sum.keys():
            sub_sum[ac_sum] = i

    return length


if __name__ == "__main__":
    arr = [7, 3, 2, 1, 1, 7, 7, 7]
    print(longest_length(arr, 7))
    arr = [7, 3, 2, 1, 1, 7, -6, -1, 7]
    print(longest_length(arr, 7))
