class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 递推公式：a[0][0] = a[0][1]+a[1][0]
        # 递归 time:O(2^n)
        # def dfs(i,j):
        #     # terminator
        #     if i == m or j == n:
        #         return 0
        #     if i == m-1 and j == n-1:
        #         return 1
        #     # process
        #     # drill down
        #     return dfs(i,j+1) + dfs(i+1,j)
        # return dfs(0,0)

        # dp:从finish->(i,j) time:O(nm) space:O(nm)
        # dp = [[0]*n]*m
        # for i in range(m)[::-1]:
        #     for j in range(n)[::-1]:
        #         # 初始值
        #         if i==m-1 or j==n-1:
        #             dp[i][j] = 1
        #         else:
        #             # DP方程 递推公式
        #             dp[i][j] = dp[i+1][j]+dp[i][j+1]
        # return dp[0][0]

        # dp:从start->(i,j) time:O(nm) space:O(nm)
        # dp = [[0]*n]*m
        # for i in range(m):
        #     for j in range(n):
        #         # 初始值
        #         if i==0 or j==0:
        #             dp[i][j] = 1
        #         else:
        #             # DP方程
        #             dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # return dp[m-1][n-1]

        # dp:从start->(i,j) time:O(nm) space:O(n)
        dp = [1]*n
        for i in range(1,m):
            for j in range(n):
                # 初始值
                if j==0:
                    dp[j] = 1
                else:
                    # DP方程 复用上一行的数据，达到降维的目的
                    dp[j] += dp[j-1]
        return dp[n-1]

        # 组合思维，从左上到右下需要移动m-1+n-1 = m+n-2次，其中m-1次向下移动，n-1次向右移动，
        # 则答案的解即为从m+n-2次移动种选取m-1次向下移动的解
        # time:O(min(m,n)) 交换行列的值不影响最终的结果 space:O(1)
        # return itertools.comb(m+n-2,m-1)