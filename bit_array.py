# 实现一个bit类型的数组0 ~ 319


arr = [0] * 10    # type(a[0]) = int, 10 * 32 = 320

index = 300
int_index = index // 32
bit_index = index % 32
print(int_index, bit_index, 1 << bit_index)
arr[int_index] = (arr[int_index] | 1 << bit_index)
print(arr[int_index])
print(arr)

index = 301
int_index = index // 32
bit_index = index % 32
print(int_index, bit_index, 1 << bit_index)
arr[int_index] = (arr[int_index] | 1 << bit_index)
print(arr[int_index])
print(arr)

