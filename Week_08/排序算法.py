# -*- coding: UTF-8 -*-

# @Created on 2021/02/24 22:35:25 周三
# @排序算法.py
# @author: xiaochuan
# @description: 常见排序算法    

import random

LENGTH = 10
arr = [random.randint(1,100) for _ in range(LENGTH)]

# 冒泡排序
def bubble_sort(arr):
    # 一共比较n-1轮
    for i in range(LENGTH-1):
        # 每轮比较次数n-1-i
        for j in range(LENGTH-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# 快排
def quick_sort(arr,left=0,right=LENGTH-1):
    # terminator
    if left >= right:
        return 
    # process curr logic
    partition_idx = partition(arr,left,right)
    # drill down
    quick_sort(arr,left,partition_idx-1)
    quick_sort(arr,partition_idx+1,right)
    # no revert
    return arr

# 快排——分区操作
def partition(arr,left,right):
    pivot,idx = left,left+1
    for i in range(idx,right+1):
        # 将小于基准值的交换到前面的
        # idx的巧妙运用 
        # ∵idx <= i,∴交换时idx索引指向的值肯定是已经比较过的，也不会对后面要比较的数早成影响
        if arr[i] < arr[pivot]:
            arr[i],arr[idx] = arr[idx],arr[i]
            idx += 1
    # 交换pivot和最后一个小于基准值的数
    arr[pivot],arr[idx-1] = arr[idx-1],arr[pivot]
    # 返回基准值所在的索引
    return idx-1
    
    
    
    
# 简单插入排序 O(n^2)
def insert_sort(arr,le = LENGTH):
    # 对数组中出第一个元素外的其它元素排序
    for i in range(1,le):
        j = i
        # 确定新元素的位置，如果前置元素>新元素，则交换
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1
    return arr

# 希尔排序(插入排序的进阶，设置增量，按增量间隔，将数组分成k个子序列，对每个子序列做简单插排)
def shell_sort(arr):
    # 设置增量为arr.length的1/2，每次倍数缩小增量
    gap = LENGTH // 2
    while gap > 0:
        # 按增量对每个子序列进行简单插排
        for i in range(gap,LENGTH):
            j = i
            while j > 0 and arr[j-gap] > arr[j]:
                arr[j-gap],arr[j] = arr[j],arr[j-gap]
                j -= gap
        gap //= 2
    return arr
    
# 选择排序（将无序区中最小的元素放在有序区的末尾（即和无序区的第一个元素交换））
def selection_sort(arr):
    # 进行N-1趟交换即可
    for i in range(LENGTH-1):
        mi = i
        # 找出无序区中最小的元素(下标)
        for j in range(i,LENGTH):
            if arr[mi] > arr[j]:
                mi = j
        # 将最小元素交换至有序区的末尾
        arr[i],arr[mi] = arr[mi],arr[i]      
    return arr

# 堆排序    
def heapq_sort(arr):
    import heapq
    # heapq.heapify(arr)
    # return [heapq.heappop(arr) for _ in range(LENGTH)]
    return heapq.nsmallest(LENGTH,arr)

# 归并排序(一分为二，然后合并两个有序数组（递归后，可以保证当前层两个子序列是有序的），递归重复)
def merge_sort(arr,left=0,right=LENGTH-1):
    # terminator
    if left >= right:
        return
    # process curr logic
    mid = (left+right)>>1
    # drill down
    merge_sort(arr,left,mid)
    merge_sort(arr,mid+1,right)
    merge(arr,left,mid,right)

    return arr

def merge(arr,left,mid,right):
    # 临时数组，用于存放排序后的数组
    temp = [0]*(right-left+1)
    i,j,k = left,mid+1,0
    # 合并两个有序数组(使用额外空间)
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    # 将排序后的数组合并至原数组
    arr[left:left+len(temp)] = temp
    



# 基数排序(基数：个十百千万，先按个位排序，再十位百位...)
def radix_sort(arr):
    import collections
    # 获取数组中最大的数，并计算位数
    ma_digit = len(str(max(arr)))
    dev = 1 # 除数
    # 基数比较，并排序
    for _ in range(ma_digit):
        res = [[] for _ in range(10)]
        for num in arr:
            # 计算每个数的当前基数
            radix = num % 10 if not _ else num // dev
            # 挂到对应字典的下方
            res[radix].append(num)
        # 除数乘10
        dev *= 10
        # 将排序后的res依次写入原数组
        start,end = 0,0
        for i in range(10):
            end += len(res[i])
            arr[start:end] = res[i]
            start = end
    return arr

# 计数排序
def count_sort(arr):
    # 计算最大最小是为了减少额外空间
    ma,mi = max(arr),min(arr)
    count = [0 for _ in range(ma-mi+1)]
    # 计数，数组对应下标数据+1
    for num in arr:
        count[num-mi] += 1
    # 填充到原数组
    start,end = 0,0
    for i in range(len(count)):
        if count[i]:
            end += count[i]
            arr[start:end] = [i+mi]*count[i]
            start = end
    
    return arr

# 桶排序（计数排序的升级版,使用映射函数，将数组数据划分为一定数量的桶，对每一个桶中数据（调用其它排序方式）进行排序）
def bucket_sort(arr):
    # 获取最大最小值
    ma = mi = arr[0]
    for num in arr:
        if ma < num:
            ma = num
        if mi > num:
            mi = num
    # 使用映射函数(这里是值映射)
    DEFAULT_BUCKET_LEN = 7
    bucket_len = (ma-mi)//DEFAULT_BUCKET_LEN + 1
    bucket = [[] for _ in range(bucket_len)]
    for num in arr:
        bucket[(num-mi)//DEFAULT_BUCKET_LEN].append(num)
    # 对每个桶中的数据进行排序，然后写入原数组中
    start,end = 0,0
    for i in range(bucket_len):
        if bucket[i]:
            bucket[i] = insert_sort(bucket[i],len(bucket[i]))
            end += len(bucket[i])
            arr[start:end] = bucket[i]
            start = end

            
    return arr


if __name__ == "__main__":
    
    print('排序之前：{}'.format(arr))
    print("")
    if not arr:
        print([])
    # print('冒泡排序：{}'.format(bubble_sort(arr[:])))
    # print('快速排序：{}'.format(quick_sort(arr[:])))
    # print('简单插入排序：{}'.format(insert_sort(arr[:])))
    # print('希尔排序：{}'.format(shell_sort(arr[:])))
    # print('选择排序：{}'.format(selection_sort(arr[:])))
    # print('堆排序：{}'.format(heapq_sort(arr[:])))
    # print('归并排序：{}'.format(merge_sort(arr[:])))

    # print('基数排序：{}'.format(radix_sort(arr[:])))
    # print('计数排序：{}'.format(count_sort(arr[:])))
    print('桶排序：{}'.format(bucket_sort(arr[:])))


    