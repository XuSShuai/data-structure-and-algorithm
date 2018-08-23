# 给定一个字符串类型的数组strs， 找到一种拼接方式， 使得把所
# 有字符串拼起来之后形成的字符串具有最低的字典序。
import functools


def comparator(str1: str, str2: str) -> int:
    string1 = str1 + str2
    string2 = str2 + str1
    if string1 < string2:
        return -1
    elif string1 > string2:
        return 1
    else:
        return 0


def lowest_dictionary_order(arr):
    arr.sort(key=functools.cmp_to_key(comparator))
    res = ""
    for r in arr:
        res += r
    print(res)


if __name__ == "__main__":
    arr = ["ba", "b"]
    lowest_dictionary_order(arr)
    arr = ["jibw", "ji", "jp", "bw", "jibw"]
    lowest_dictionary_order(arr)