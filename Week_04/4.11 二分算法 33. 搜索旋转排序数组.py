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
        
        while left <= right:
            mid = left + (right-left)//2
            if target == nums[mid]:
                return mid
            elif (nums[0] <= target) ^ (target < nums[mid]) ^ (nums[mid] <= nums[0]):
                left = mid - 1
            else:
                right = mid + 1

        return -1
        

if __name__ == "__main__":
    nums = [3,5,1]
    target = 3
    print(Solution().search(nums,target))