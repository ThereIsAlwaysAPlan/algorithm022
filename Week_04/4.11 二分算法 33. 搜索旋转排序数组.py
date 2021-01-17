#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-14 18:52:21
# @Author: xiaochuan
# @Description: 33. 搜索旋转排序数组    
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        # while left <= right:
        #     mid = left + (right-left)//2
        #     if target == nums[mid]:
        #         return mid
        #     else:
        #         if nums[left] > nums[right]:
        #             # 发生了旋转
        #             # 在左边
        #             if nums[right] >= nums[mid] and (target < nums[mid] or target >= nums[left]) or nums[left] < nums[mid] and target >= nums[left] and target <= nums[mid]:
        #                 right = mid - 1  
        #             # 在右边
        #             else:
        #                 left = mid + 1
        #         else:
        #             # 未发生旋转
        #             # 在左边
        #             if target < nums[mid]:
        #                 right = mid - 1
        #             else:
        #                 left = mid + 1 
        

        # 二分的定义是对于一个有序或者部分有序数组，通过取中值比对目标数值，每次筛除一半数据，而对另一半数据下一次筛除，
        # 要牢记的一点是选择舒适区，对于容易归纳的部分，我们首先提取出来，作为分割的一半，那么剩下的一半，无论多么复杂，也只是属于"else"的情况
        # 总体思路：
        # 考虑 mid位置，在左边的升序数组还是在右边的升序数组
        # 再只考虑target在start ~ mid(若在左边) 或者 mid ~ end(若在右边)的请况即可排除其它情况
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            else:
                # 根据mid在旋转点左右哪边进行划分
                if nums[0] <= nums[mid]:
                    if nums[0] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] < target <= nums[-1]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
        

if __name__ == "__main__":
    nums = [3,5,1]
    target = 3
    print(Solution().search(nums,target))