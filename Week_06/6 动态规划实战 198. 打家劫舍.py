from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 递归，回溯，尝试所有的偷窃方式，记录最大值
        # 重复性，当天晚上偷，第二天不能偷，当天晚上不偷，第二天可偷可不偷
        # 2^n   timeout
        # res = [0]
        # length = len(nums)
        # def dfs(level,money,flag):
        #     # terminator
        #     if level == length:
        #         res[0] = max(res[0],money)
        #         return 
        #     # process curr logic
        #     # drill down
        #     if flag:
        #         # 昨天偷
        #         dfs(level+1,money+nums[level],False)
        #     else:
        #         # 昨天不偷
        #         dfs(level+1,money,False)
        #         dfs(level+1,money,True)
        # dfs(0,0,False)
        # dfs(0,0,True)
        # return res[0]

        # DP dp[i]表示到第i天可偷窃到的最大金额（但是不知道第i天偷不偷）
        # 加个状态：  0：不偷，1偷
        # 重复性 pro(i,0) = max(sub(i-1,0),sub(i-1,1)) pro(i,1) = sub(i-1,0) + nums[i]
        # dp array f[i][0,1]
        # dp equation
        # time:O(N) space:O(n)
        # length = len(nums)
        # if not nums:
        #     return 0
        # dp = [[0]*2 for _ in range(length)]
        # dp[0] = [0,nums[0]]
        # for i in range(1,length):
        #     dp[i][0] = max(dp[i-1][0],dp[i-1][1])
        #     dp[i][1] = dp[i-1][0] + nums[i]
        # return max(dp[-1])

        # DP优化1：dp[i]表示到第i天可偷盗的最大金额
        # 子问题，第i天可偷可不偷，两者取最大 dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        # if not nums:
        #     return 0
        # length = len(nums)
        # dp = [0]*len(nums)
        # dp[0] = nums[0]
        # if length < 2:
        #     return nums[0]
        # dp[1] = max(nums[0],nums[1])
        # for i in range(2,len(nums)):
        #     dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        # return dp[-1]

        # DP优化2：最终结果只跟其前两天的状态有关
        prev = curr = 0
        for num in nums:
            prev,curr = curr,max(curr,num+prev)
        return curr