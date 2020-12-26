#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2020-12-26 16:55:28
# @Author: xiaochuan
# @Description: 两数之和(亚马逊、字节跳动、谷歌、Facebook、苹果、微软、腾讯在半年内面试中常考)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力 O(n^2)
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        # hashtable  one/two times   time:O(n) space:O(n)
        # a = target - b   dict[nums[i]] = i judge target-b in dict? 
        # 延申： 3Sums  ： -c = a + b   4Sums...NSums
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i,d[target-nums[i]]]
            d[nums[i]] = i
        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9        
    print(Solution().twoSum(nums,target))