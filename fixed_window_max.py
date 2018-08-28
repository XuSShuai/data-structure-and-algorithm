# 生成窗口最大值数组

# 对一个整形数组arr使用一个大小为w的窗口从数组的最左边滑动到最右边，窗口每次向右边滑动一个位置
# 如果数组的长度为n，窗口的大小为w，则一共产生n-w+1个窗口中的最大值。

# 4 3 5 4 3 3 6 7
# [4 3 5] 4 3 3 6 7 -> 5
# 4 3 5 [4 3 3] 6 7 -> 4
# 4 3 5 4 3 [3 6 7] -> 7

# 返回5, 5, 5, 4, 6, 7

# d=deque([])           # 创建一个空的双队列
# d.append(item)        # 在d的右边(末尾)添加项目item
# d.appendleft(item)    # 从d的左边(开始)添加项目item
# d.clear()             # 清空队列，也就是删除d中的所有项目
# d.extend(iterator)    # 在d的右边(末尾)添加iterator中的所有项目
# d.extendleft(item)    # 在d的左边(开始)添加item中的所有项目
# d.pop()               # 删除并返回d中的最后一个(最右边的)项目。如果d为空，则引发IndexError
# d.popleft()           # 删除并返回d中的第一个(最左边的)项目。如果d为空，则引发IndexError
# d.count(n)            # 在队列中统计元素的分数，n表示统计的元素
# d.remove(n)           # 从队列中删除指定的值
# d.reverse()           # 翻转队列
# d.rotate(n=1)         # 将d向右旋转n步(如果n<0，则向左旋转)


from collections import deque


def fixed_windows_max(arr, w):
    res = []
    dou_end_queue = deque([])
    for i in range(len(arr)):
        while len(dou_end_queue) != 0 and arr[dou_end_queue[len(dou_end_queue) - 1]] <= arr[i]:
            dou_end_queue.pop()
        dou_end_queue.append(i)
        if i - w == dou_end_queue[0]:
            dou_end_queue.popleft()
        if i - w >= -1:
            res.append(arr[dou_end_queue[0]])
    return res

if __name__ == "__main__":
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    res = fixed_windows_max(arr, 3)
    print(res)

