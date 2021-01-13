#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-13 23:14:18
# @Author: xiaochuan
# @Description: 122. 买卖股票的最佳时机 II
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心：只要第二天的价格超过第一天，就在第一天买，第二天卖，循环这样的操作，最后所得到的利润就是最大利润
        # if len(prices) < 2:
        #     return 0
        # count = 0
        # for i in range(1,len(prices)):
        #     if prices[i-1] < prices[i]:
        #         count += prices[i]-prices[i-1]
        # return count

        # 动态规划 dp：利润  
        # dp[i][0]:当日未持有的最大利润 dp[i][1]:当日持有的最大利润
        # 当日持有  =  昨日持有 or 昨日未持有 - 今日买入花销
        # 当日未持有 = 昨日未持有 or 昨日持有 + 今日卖出所得
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0] = [0,-prices[0]]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i])
        return dp[n-1][0]

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))