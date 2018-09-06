# data-structure-and-algorithm

### part 1

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
 - [small_sum_merge_sort.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/small_sum_merge_sort.py)：归并排序的一个应用。
  在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和，求一个数组的小和。
  例子：\
  [1,3,4,2,5]\
  1左边比1小的数， 没有\
  3左边比3小的数， 1\
  4左边比4小的数， 1、 3\
  2左边比2小的数， 1\
  5左边比5小的数， 1、 3、 4、 2\
  所以小和为1+1+3+1+1+3+4+2=16\
  利用**归并排序的思想**，1在和3进行合并的时候，res+1， 1,3作为一个整体在和4,2,5进行合并的时候，对于1来说，res+1（由于4）、res+1（由于2）、res+1（由于5）；对于3来说，res+3（由于4）、res+3（由于5）
 - [inverse_pair.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/inverse_pair.py)：逆序对问题，
在一个数组中， 左边的数如果比右边的数大， 则两个数构成一个逆序对， 请打印所有逆序对。例子：1,3,4,2,5,1\
所有的逆序对有：\
3, 2\
4, 2\
3, 1\
4, 1\
2, 1\
5, 1

### part 2
  
  - [netherland_flag.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/netherland_flag.py)：荷兰国旗问题，给定一个数组arr， 和一个数num， 请把小于num的数放在数组的左边， 等于num的数放在数组的中间， 大于num的数放在数组的右边。要求额外空间复杂度O(1)， 时间复杂度O(N)。
  - [quick_sort.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/quick_sort.py)：快速排序。利用荷兰国旗问题对经典的快排算法进行改进，将数组的最后的一个数选为pivot，小于pivot的放在左边；等于的放在中间；大于的放在右边。再对左边区域和右边区域递归此过程。
  - [random_quick_sort.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/random_quick_sort.py)，随机快排，仅仅是将pivot的选择从每次的最后一个元素设置变为随机。这样快排的时间复杂度的长期期望为$O(N\log{N})$。额外空间复杂度为$O(\log{N})$
  - [heap_sort.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/heap_sort.py)：堆在逻辑上就是一棵完全二叉树，一个下标为$i$的节点的左右孩子节点的下标分别为$2\*i+1$和$2\*i+2$， 父节点的下标为$\frac{i-1}{2}$。
    - 大根堆：在一棵完全二叉树中，任何一棵子树中的最大值都位于头结点上；
    - 小根堆：在一棵完全二叉树中，任何一棵子树中的最小值都位于头结点上；\
长度为N的数组调整为大（小）根堆的时间复杂度为$O(N) = \log{1} + \log{2} + ... + \log{(N-1)}$。也就是heap_insert的时间复杂度为$O(N)$；\
heapify的时间复杂度$O(\log{N})$。\
堆排序的时间复杂度为$O(N\log{N})$。

- 算法的稳定性分析：
  - $O(N^2)$
    - 冒泡排序可以实现成稳定的排序算法，当两个数相等的时候不进行交换。
    - 插入排序可以实现成稳定的排序算法。
    - 选择排序是不稳定的。
