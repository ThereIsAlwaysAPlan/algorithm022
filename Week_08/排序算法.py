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
    
    
    
    
# 简单插入排序
def insert_sort(arr):
    return None

# 希尔排序
def shell_sort(arr):
    return 
    
# 选择排序
def selection_sort(arr):
    return 

# 堆排序    
def heapq_sort(arr):
    return None

# 归并排序
def merge_sort(arr):
    return None

# 基数排序
def radix_sort(arr):
    return None

# 计数排序
def count_sort(arr):
    return None

# 桶排序
def bucket_sort(arr):
    return None


if __name__ == "__main__":
    print('排序之前：{}'.format(arr))
    print("")
    # print('冒泡排序：{}'.format(bubble_sort(arr[:])))
    print('快速排序：{}'.format(quick_sort(arr[:])))
    