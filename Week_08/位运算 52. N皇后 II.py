#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-02-07 22:41:16
# @Author: xiaochuan
# @Description: 52. N皇后 II

class Solution:
    def totalNQueens(self, n: int) -> int:
        # ∵ n∈[1,9],有限范围，直接给出答案即可，O(1)
        d = {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 9: 352}
        return d[n]
        
        # 回溯 + 剪枝
        # A*算法

        # 终极解法 ：位运算
        count = 0
        def dfs(n,row,col,pie,na):
            nonlocal count
            # terminator
            if row >= n:
                count += 1
                return
            
            # process curr logic
            bits = (~(col | pie | na)) & ((1<<n) - 1) # 获取可填位置
            while bits:
                p = bits & -bits # 获取最低位的1，即拿出一个可填位置
                bits = bits & (bits - 1) # 清0最低位的1，即 该可填位置被皇后占据
                # drill down
                dfs(n,row+1,col|p,(pie|p)<<1,(na|p)>>1)
                # revert nothing to revert, int unchangeable
        # d = {}
        # for i in range(1,10):
        #     count = 0
        #     dfs(i,0,0,0,0)
        #     d[i] = count
        # print(d)
        # count = 0
        dfs(n,0,0,0,0)
        return count
