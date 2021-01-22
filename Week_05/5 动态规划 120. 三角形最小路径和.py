# 1.枚举所有路径，找出最小的那个（循环，递归）time:O(2^n)
# 2.DP
# a.分治 problems(i,j) = min(sub(i+1,j),sub(i+1,j+1))+a[i,j]，其中，problems(i,j)表示第i层的最小路径和
# b.DP array triangle
# c.DP 方程 f[i,j] = min(f[i+1,j],f[i+1,j+1])+triangle[i,j]  
# 自底向上，因为可以确定，最小路径和肯定要穿过最后一排中的一个，以此向上依次得出当前行的最小路径和，这样得出的是无后效性的，是完全包含的
# 和面试官沟通：「是否有空间复杂度限制」「是否可以修改原数组」等等，
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        # 二维 time:O(n^2) space:O(n^2)
        # dp = triangle
        # for i in range(length-1)[::-1]:
        #     for j in range(len(triangle[i])):
        #         dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
        # return dp[0][0]

        # 滚动数组思想 time:O(n^2) space:O(n)
        dp = triangle[-1][:]
        for i in range(length-1)[::-1]:
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
        return dp[0]