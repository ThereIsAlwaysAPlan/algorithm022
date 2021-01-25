from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 环问题，分解成两个单链问题
        # 即 第0天偷，则最后一天不偷，计算2~n-1；第0天不偷，则最后一天可偷，计算1~n,两者取最大
        if not nums:
            return 0
        prev = curr = 0
        for num in nums[2:-1]:
            prev,curr = curr,max(curr,num+prev)
        num1=curr+nums[0]
        prev = curr = 0
        for num in nums[1:]:
            prev,curr = curr,max(curr,num+prev)
        return max(num1,curr)