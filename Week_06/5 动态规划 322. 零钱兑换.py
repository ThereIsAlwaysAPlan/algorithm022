# 1.暴力
# 2.bfs 每一步可走到的距离
# 3.递归
# 4.dp 记到总金额为i最少的硬币个数为fi
# a.subproblems : problems(i) = min(sub(i-k)+1 k in coins) 
# b.dp array fn
# c.dp equation fn = min(f(n-k), k in coins)+1
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bfs 双指针 time:O(2^n)
        # coins.sort(reverse=True) # 让数大的硬币先递归，减少递归次数
        # if amount in coins:
        #     return 1
        # if amount < 1:
        #     return 0
        # find = set()
        # count = 1 # 计数
        # curr = coins
        # while curr:
        #     nxt = []
        #     count += 1
        #     for value in curr:
        #         # 加硬币
        #         for i in coins:
        #             if value + i == amount:
        #                 return count
        #             elif value + i > amount:
        #                 continue
        #             if value+i not in find:
        #                 find.add(value+i)
        #                 nxt.append(value+i)
        #     curr = nxt
        # return -1

        # DP
        # 自顶向下 递归
        
        
        # DP
        # 初始化 自底向上
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        # dp方程
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1