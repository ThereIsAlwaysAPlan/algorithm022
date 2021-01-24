from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DP
        # 初始化
        # 刚开始就没路
        if obstacleGrid[0][0] == 1: return 0 # [[1,0]]

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        # 初始化首行元素
        dp = [0]*col
        for j in range(col):
            # 首行遇到障碍，后面的都不能走
            if obstacleGrid[0][j] == 1:
                break
            dp[j] = 1
        
        for i in range(1,row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0 and obstacleGrid[i][j-1] == 0:
                    dp[j] += dp[j-1]
                    
            print(dp)
        return dp[col-1]