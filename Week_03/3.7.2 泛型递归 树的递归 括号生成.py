#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-02 21:56:47
# @Author: xiaochuan
# @Description: 
from typing import List

# 合法括号
# left 左括号随时可以加，只要不超过n个
# right 右<左
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 递归
        # res = []
        # 没有考虑有效括号
        # def _generator(level,max_level,s):
        #     if level > max_level:
        #         res.append(s)
        #         return
        #     # process current logic

        #     # drill down
        #     _generator(level+1,max_level,s + "(")
        #     _generator(level+1,max_level,s + ")")
        # _generator(1,2*n,"")
        
        # 加上合法规则
        # def _generator1(left,right,max_level,s):
        #     if left == max_level and right == max_level:
        #         res.append(s)
        #         return
        #     # process current logic

        #     # drill down
        #     if left < n:
        #         _generator1(left+1,right,max_level,s + "(")
        #     if right < left:
        #         _generator1(left,right+1,max_level,s + ")")
        
        # _generator1(0,0,n,"")
        # return res

        # 动态规划
        if not n:
            return []
        all_res = [[""],["()"]] # n=0,1
        for i in range(2,n+1):
            tmp_res = []
            for j in range(i):
                p = all_res[j]
                q = all_res[i-1-j]
                for x in p:
                    for y in q:
                        tmp_res.append("(" + x + ")" + y)
            all_res.append(tmp_res)
        return all_res[n]

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))