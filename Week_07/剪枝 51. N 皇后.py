#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-29 00:44:14
# @Author: xiaochuan
# @Description: 51. N 皇后
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 回溯 + 剪枝
        # 初始化，col，pie，na
        # if n < 1:
        #     return []36. 有效的数独
        # col,pie,na = set(),set(),set()
        # res = []
        # def dfs(n,i,tmp):
        #     # terminator
        #     if i == n:
        #         res.append(tmp)
        #         return
            
        #     # process current logic
        #     for j in range(n):
        #         if j in col or i+j in pie or i-j in na:
        #             continue
        #         col.add(j)
        #         pie.add(i+j)
        #         na.add(i-j)
        #         dfs(n,i+1,tmp+[j])
        #         col.remove(j)
        #         pie.remove(i+j)
        #         na.remove(i-j)
        # dfs(n,0,[])
        # return [['.'*j + 'Q' + '.'*(n-j-1) for j in tmp] for tmp in res]

        # 回溯+剪枝 写法优化
        if n < 1:
            return []
        res =[]
        def dfs(queens,pie,na):
            i = len(queens)
            if i == n:
                res.append(queens)
                return
            
            for j in range(n):
                if j not in queens and i+j not in pie and i-j not in na:
                    dfs(queens+[j],pie+[i+j],na+[i-j])
        dfs([],[],[])
        return [['.'*j + 'Q' + '.'*(n-j-1) for j in tmp] for tmp in res]