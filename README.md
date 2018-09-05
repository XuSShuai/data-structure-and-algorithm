# data-structure-and-algorithm

 - bubble_sort.py: 冒泡排序，$O(N^2)$，额外空间复杂度$O(1)$。
 - selection_sort.py: 选择排序，$O(N^2)$，额外空间复杂度$O(1)$。
 - insert_sort.py: 插入排序，
    - 时间复杂度分析：冒泡排序和选择排序的时间复杂度严格$O(N^2)$，对于插入排序，如果待排序数组有序，则时间复杂度为$O(N)$；
    若初始数组逆序，则时间复杂度为$O(N^2)$。根据时间复杂度的定义，该算法时间复杂度为$O(N^2)$。额外空间复杂度$O(1)$。
 - get_max.py:求数组中最大值，熟悉递归操作。（调用子函数时候父函数运行环境被系统自动压栈）
    - `master公`式（递归函数时间复杂度分析）:$$T(N) = aT(\frac{n}{b})+O(n^d)$$
        - 如果$\logba > d$，时间复杂度为：$O(N^{logba})$
        - 如果$\logba = d$，时间复杂度为：$O(N^d*{logN})$
        - 如果$\logba < d$，时间复杂度为：$O(N^d)$
