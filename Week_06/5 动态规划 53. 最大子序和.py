# 1.暴力，求出所有的连续子数组的和，取最大即可，time:O(n^2)
# 2.DP  
# a.重复性，用p[i]表示到i为止的最大和，那么有 
# 如果是包含当前值i，那么只有两种情况，1.之前累加和为负数，那么我们进行止损，丢弃之前的数据，至今为止，最大值就是自身，如果累加和为正数，那么加上之前的累加和即可
# p(i) = max(p(i-1)+nums[i],nums[i]) 
# b.DP array fn
# c.DP euqation  fi = max(f(i-1)+nums[i],nums[i])
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # space:O(n)
        length = len(nums)
        # 一维
        # dp =[0]*length
        # dp[0] = nums[0]
        # for i in range(1,length):
        #     dp[i] = max(dp[i-1],0)+nums[i]
        # return max(dp)
        # 常数
        # res = prev=dp=nums[0]
        # for i in range(1,length):
        #     dp = max(prev,0)+nums[i]
        #     prev = dp
        #     res = max(res,dp)
        # return res


        # 原地
        for i in range(1,length):
            nums[i] += max(nums[i-1],0)
        return max(nums)