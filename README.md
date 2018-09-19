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
  - $O(N\log{N})$
    - 归并可以
    - 快排不可以
    - 堆排序不可以
综合排序算法：当数据量很大的时候，如果是基础数据类型，使用快排（不需要稳定性）；如果是自定义数据类型，使用归并排序（需要有稳定性）。如果数据量很小，使用插入排序。

### part 3

 - 使用定长数组实现栈和队列
   - [stack_based_array.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/stack_based_array.py)
   - [queue_based_array.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/queue_based_array.py)

     在python中可以引入queue包来使用封装好的栈和队列，`queue.LifoQueue(-1)`为栈；`queue.Queue(-1)`为队列。[queue_api.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/queue_api.py)\
     `q.qsize()` 返回大小\
     `q.empty()` 如果为空，返回True,反之False\
     `q.full()` 如果满了，返回True,反之False\
     `q.get()` \
     `q.put(item)` 
     
  - 仅用队列实现栈结构：[quene2stack.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/quene2stack.py)
  - 仅用栈实现队列结构：[stack2queue.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/stack2queue.py)

### part 4

 - 转圈打印矩阵：[print_matrix_spiral_order.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/print_matrix_spiral_order.py), 例如对于矩阵：\
  $$
  \left[
  \begin{matrix}
    0 & 1 & 2 & 3 & 4 & 5\\\\
    6 & 7 & 8 & 9& 10& 11\\\\
    12& 13& 14& 15& 16& 17\\\\
    18& 19& 20& 21& 22& 23\\\\
  \end{matrix}
  \right]
  $$
    输出打印结果为：0 1 2 3 4 5 11 17 23 22 21 20 19 18 12 6 7 8 9 10 16 15 14 13 
    
 - 旋转打印矩阵：[rotate_matrix.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/rotate_matrix.py)
   对矩阵旋转90度，例如：\
   $$
   \left[
   \begin{matrix}
    0 & 1 & 2 & 3 & 4\\\\
    5 & 6 & 7 & 8 & 9\\\\
    10 &11 &12 &13 &14\\\\
    15 &16 &17 &18 &19\\\\
    20 &21 &22 &23 &24\\\\
   \end{matrix}
   \right]
   $$
   旋转之后的输出为：\
   $$
   \left[
   \begin{matrix}
    20 &15 &10 & 5 & 0\\\\
    21 &16 &11  &6 & 1\\\\
    22 &17 &12 & 7 & 2\\\\
    23& 18& 13&  8&  3\\\\
    24& 19& 14&  9&  4
   \end{matrix}
   \right]
   $$
 - 之字形打印矩阵：[zig_zag_print.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/zig_zag_print.py)\
   对矩阵\
   $$
   \left[
   \begin{matrix}
    0 & 1 & 2 & 3 & 4 \\\\
    5 & 6 & 7 & 8 & 9 \\\\
    10& 11& 12& 13& 14 \\\\
    15& 16& 17& 18& 19
   \end{matrix}
   \right]
   $$
   的打印结果为：0 1 5 10 6 2 3 7 11 15 16 12 8 4 9 13 17 18 14 19
   
 - 反转单向链表：[reverse_list.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/reverse_list.py)，要求时间复杂度为$O(N)$，额外空间复杂度为$O(1)$。
 - 反转双向链表：[reverse_double_list.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/reverse_double_list.py)，要求时间复杂度为$O(N)$，额外空间复杂度为$O(1)$。

 - 判断一个链表是否为回文结构：[is_palindrome_list.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/is_palindrome_list.py)
    - 方法1：额外空间复杂度为$O(N)$，对链表进行遍历，并将元素一一入栈，第二次遍历时和栈中弹出的元素比较，如果存在不相等的，则不是回文。
    - 方法2：额外空间复杂度$O(N/2)$，使用快慢指针，慢指针从找到的中点位置之后开始将元素入栈（一半的链表元素），入栈完成后，重新遍历链表和栈中依次弹出的元素对比，如果栈空之前发现有不等的元素，则不是回文结构。
    - 方法3：额外空间复杂度$O(1)$，使用快慢指针，将慢指针之后的链表逆序，然后分别从第一个节点往后和最后一个节点往前逐个开始进行比对。


 - [copy_link_with_two_point.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/copy_link_with_two_point.py)复制含有随机指针节点的链表
      一种特殊的链表节点类描述如下：
      ```java
      public class Node {
        public int value;
        public Node next;
        public Node rand;
        public Node(int data) {
            this.value = data;
        }
      }
      ```

      Node类中的value是节点值， next指针和正常单链表中next指针的意义一样，都指向下一个节点，
      rand指针是Node类中新增的指针， 这个指针可能指向链表中的任意一个节点， 也可能指向null。
      给定一个由Node节点类型组成的无环单链表的头节点head， 请实现一个函数完成这个链表中所有
      结构的复制， 并返回复制的新链表的头节点。
      进阶：
      不使用额外的数据结构， 只用有限几个变量， 且在时间复杂度为O(N)内完成原问题要实现的函数。
      
 - [intersect_node.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/intersect_node.py)**两个单链表相交的一系列问题**：在本题中,单链表可能有环,也可能无环.给定两个单链表的头节点head1和head2,这两个链表可能相交,也可能不相交. 请实现一个函数,如果两个链表相交,请返回相交的第一个节点;如果不相交,返回null即可.要求:如果链表1的长度为N， 链表2的长度为M，时间复杂度请达到 O(N+M)， 额外空间复杂度请达到O(1)。
      - 第一个问题：如何判断一个单链表是否有环。
          - 方法一：使用一个hashmap（在python中可以使用一个set或者是dict结构），从头节点开始遍历并将节点放入到哈希表中，在放入的过程中如果发现哈希表中已经存在该节点，则说明有环，并且该节点是第一个入环的节点；如果遍历到空，则说明无环。
          - 方法二：使用一个快指针，如果快指针在遍历的过程中发现空，则无环；否则在快指针和慢指针相遇的时候，快指针回到头结点，快指针和慢指针都一次走一步，相遇的节点是第一个入环的节点。
      - 第二个问题：当已经知道两个单链表各自是否有环的情况下，如何判断第一个相交的节点：
          - 如果两个单链表都没有环：
               - 方法一：哈希表：将单链表1中的所有节点放入哈希表中，遍历单链表2的每一个节点，第一个存在于哈希表中的属于单链表二的节点为相交的节点；如果不存在这样的节点，则不相交。
               - 方法二：统计单链表1的长度L1和最后一个节点end1，单链表2的长度L2和最后一个节点end2。如果end1!=end2，不相交；如果end1==end2，相交，从头结点开始，较长的单链表先走两个链表相差的步数，然后开始一起走，第一个相同的节点为入环的第一个节点。
          - 如果一个有环，一个无环：不可能相交。
          - 两个环分三种情况。
        
 
### part 5

 - 二叉树的遍历：[traversal_binary_tree.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/traversal_binary_tree.py)
 
      - 非递归前序：出栈一个元素并打印，该元素右不为空，右进栈，左不为空，左进栈
      - 非递归中序：当前元素不为空则进栈左走，为空则出栈打印右走
      - 非递归后续：利用前序改
      - 层序遍历：使用队列
      
 - 找后继节点：[successor_node.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/successor_node.py)
 节点的类型定义为：
   ```python
   class Node:
      def __init__(self, data):
          self.data = data
          self.parent = None
          self.left = None
          self.right = None
   ```
    如果右孩子不为空，找右子树上的最左节点并返回；如果右孩子为空，向上走，直到该节点是parent节点的左孩子为止，返回parent节点。
 
 - 二叉树的序列化和反序列化：[serialize_binary_tree.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/serialize_binary_tree.py), 可以按照先序，中序，后序，层序进行序列化，使用一个队列结构进行相应的反序列化。
 
 - 判断一棵树是否是平衡二叉树：[is_balance.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/is_balance.py)

 - 是否是搜索二叉树：[is_BST.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/is_BST.py)，利用中序遍历判断是否每一个节点都比上一个节点的值大即可。
 
 - 是否是完全二叉树：[is_CBT.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/is_CBT.py)
     - 按层遍历的过程中：
         - 如果一个节点有右孩子，而没有左孩子，一定不是完全二叉树；
         - 如果一个节点不是左右孩子双全，则从现在开始以后按照层序遍历的节点必须都是叶子节点。
         
 - [complete_tree_node_number.py](https://github.com/XuSShuai/data-structure-and-algorithm/blob/master/complete_tree_node_number.py)：已知一棵完全二叉树，求其节点的个数，要求时间复杂度低于$O(N)$，N为节点的个数(所以不能使用遍历的方式)。
 
      - 公式：一棵满二叉树的节点的个数为$2^L - 1$，其中$L$为树的高度。思路：遍历根的左边界，可以得到树的总层数；遍历根的右子树的左边界；
    
         - 根的右子树的左边界达到了树的总层数，则根的左子树为满二叉树，利用公式求，然后递归求解根的右子树（此时为完全二叉树）
         - 根的右子树的左边界没有达到了树的总层数，则根的右子树为满二叉树，利用公式求，然后递归求解根的左子树（此时为完全二叉树）
    
    该算法的时间复杂度$O((log N)^2)$
     
### part 6

  - 哈希函数：
       - 输入域是无穷大的
       - 输出域是有穷的
       - same input, same output
       - 因为性质1性质2，所以不同的输入可能有相同的输出
       - 输出域上的值均匀分布
  - 哈希表
       - 数组加链表实现，初始化时给一个定长为 N 的数组 H，`put(key, value)`时，计算`index=hash(key)%N`，将该记录挂在数组中`H[index]`的链表上（java中是一棵红黑树）。根据`hash`函数的性质，每一个数据元素上挂载的链表的长度应该是几乎相等的，当该长度大于阈值时候，进行hash表的扩容。\
  实例：一个大小为100T的文件，每行一个字符串文本，如何统计重复的字符串文本。(利用哈希函数相同输入相同输出，不同输出均匀分布的特点)\
  假设有 N 台机器可用，利用hash函数计算每一行文本的hashcode，然后模 N， 这样文本被几乎均分至 N 台机器，且能保证相同的文本必定存在于同一台机器上。

  - 布隆过滤器：
       - 应用场景：现有一个100亿个url组成的黑名单，如果判断任意给定的一个url是否属于该给黑名单。
       - 问题分析：假设每一个usr为64个字节，如果使用hashset，则需要的内存大小为6400亿个字节，大约为640G。
       - 布隆过滤器的作用是实现查找某一个key是否在set中。但是存在失误率：不在set中的key可能会误报为存在于set中，但是存在set中的key异能能够被检测出来。
