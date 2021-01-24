# 1.暴力，求出str1的所有子序列，并判断是否在str2中O(n)，从后往前推，找到就返回长度
# 2.DP 自底向上 看成由两个str组成的一个二维数组
# a.重复性(反向思维) 看最后一个字符是否相等
# ① 相等 problems[i,j] = sub[i-1,j-1] + 1
# ② 不等 problems[i,j] = max(sub[i-1,j],sub[i,j-1],sub[i-1,j-1]) # 最后一项可省略，求解sub[i-1,j]时会再求解一次
# b.DP array f[i,j]
# c.DP方程 f[i,j] = f[i-1,j-1]+1 if i==j else max(f[i-1,j],f[i,j-1])
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        if m*n == 0:
            return 0
        # dp = [[0 for j in range(n)] for i in range(m)]
        # # 初始化 二维 自底向上
        # if text1[0] in text2:
        #     for j in range(text2.index(text1[0]),n):
        #         dp[0][j] = 1
        # if text2[0] in text1:
        #     for i in range(text1.index(text2[0]),m):
        #         dp[i][0] = 1
        
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = dp[i-1][j-1]+1 if text1[i] == text2[j] else max(dp[i-1][j],dp[i][j-1])
        # print(dp)
        # return dp[m-1][n-1]
            
        # 滚动数组思想
        dp = [0]*n
        if text1[0] in text2:
            for j in range(text2.index(text1[0]),n):
                dp[j] = 1
        change = n
        if text2[0] in text1:
            change = text1.index(text2[0])
        print(dp)
        for i in range(1,m):
            # prev 记录dp(i-1,j-1)
            prev = dp[0]
            for j in range(n):
                if j == 0:
                    if i >= change:
                        dp[j] = 1
                else:
                    # curr 记录当前要改变的值，并在值改变之后将未改变的值赋值给prev，相当于保存了(i-1,j-1)处的值
                    curr = dp[j]
                    if text1[i] == text2[j]:
                        dp[j] = prev+1
                    else:
                        dp[j] = max(dp[j],dp[j-1])
                    prev = curr
            print(dp)
        return dp[n-1]