# -*- coding: UTF-8 -*-

# @Created on 2021/02/21 22:54:46 周日
# @72. 编辑距离.py
# @author: xiaochuan
# @description: 高级DP

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 1.two_end BFS 代完善

        # 2.DP
        # 状态：dp(i,j)
        # DP方程： dp(i,j) = dp(i-1,j-1) if w1[i-1] == w2[j-1] else min(dp(i-1,j-1),dp(i,j-1),dp(i-1,j)) + 1
        m,n = len(word1),len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)] 
          
        # 初始化
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        # DP递推
        for i in range(1,m+1):
            # dp[i][0] = i
            for j in range(1,n+1):
                # dp[0][j] = j
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        return dp[-1][-1]