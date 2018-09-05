# data-structure-and-algorithm

 - [bubble_sort.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/bubble_sort.py): 冒泡排序，$O(N^2)$，额外空间复杂度$O(1)$。
 - [selection_sort.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/selection_sort.py): 选择排序，$O(N^2)$，额外空间复杂度$O(1)$。
 - [insert_sort.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/insert_sort.py): 插入排序，
    - 时间复杂度分析：冒泡排序和选择排序的时间复杂度严格$O(N^2)$，对于插入排序，如果待排序数组有序，则时间复杂度为$O(N)$；
    若初始数组逆序，则时间复杂度为$O(N^2)$。根据时间复杂度的定义，该算法时间复杂度为$O(N^2)$。额外空间复杂度$O(1)$。
 - [get_max.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/get_max.py):求数组中最大值，熟悉递归操作。（调用子函数时候父函数运行环境被系统自动压栈）
    - `master`公式（递归函数时间复杂度分析）:$$T(N) = aT(\frac{N}{b})+O(N^d)$$
        - 如果$\log_{b}a > d$，时间复杂度为：$O(N^{\log_ba})$
        - 如果$\log_ba = d$，时间复杂度为：$O(N^d*{\log{N}})$
        - 如果$\log_ba < d$，时间复杂度为：$O(N^d)$
 - [merge_sort.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/merge_sort.py): 归并排序，左部分排好序，右部分排好序，使用外排和一个辅助数组将左部分和右部分排好序。根据`master`公式可以得到：$$T(N) = 2T(\frac{N}{2})+O(N^1)$$ $\log_ba = 1, d = 1$, 所以归并排序的时间复杂度为$O(N\log{N})$。额外空间复杂度$O(N)$。
 - small_sum_merge_sort.py：归并排序的一个应用。
  在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和，求一个数组的小和
  例子：
  [1,3,4,2,5]
  1左边比1小的数， 没有
  3左边比3小的数， 1
  4左边比4小的数， 1、 3
  2左边比2小的数， 1
  5左边比5小的数， 1、 3、 4、 2
  所以小和为1+1+3+1+1+3+4+2=16
