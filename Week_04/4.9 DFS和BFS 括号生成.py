from typing import List
# 思路一 递归
# 合法括号
# left 左括号随时可以加，只要不超过n个
# right 右<左

# 思路二 动态规划，新生成的括号，要么在里面，要么在外面 即 fn = (p)q  ，其中，p、q是x种括号放置的方法，p+q是n-1个括号
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 递归
        # res = []

        # def dfs(left,right,n,s):
        #     # terminator
        #     if left == n and right == n:
        #         res.append(s)
        #         return
            
        #     # process current logic
        #     # drill down
        #     if left < n:
        #         dfs(left+1,right,n,s+"(")
        #     if right < left:
        #         dfs(left,right+1,n,s+")")
        #     # revert current logic

        # 递归  fn = (p)q 去重 还有有重复，时间复杂度高 舍弃
        # res = []
        # se = set()
        # if n == 0:
        #     return []

        # def dfs(level,n,s):
        #     if level == n:
        #         if s not in se:
        #             se.add(s)
        #             res.append(s)
        #         return
            
        #     for i in range(len(s)):
        #         if s[i] == "(":
        #             # 内部
        #             dfs(level+1,n,s[:i+1] + "()" + s[i+1:])
        #             # 外部 找到i之后第一个）
        #             j = i+1
        #             while s[j] == "(":
        #                 j+=1
        #             dfs(level+1,n,s[:j+1] + "()" + s[j+1:])
        # dfs(1,n,"()")
        # return res

            

        # dfs(0,0,n,"")
        # return res

        # 动态规划 fn = (p)q  p+q = fn-1
        res = [[""],["()"]]
        if n < 2:
            return res[n]
        for i in range(2,n+1):
            tmp_res = []
            for j in range(i):
                for x in res[j]:
                    for y in res[i-1-j]:
                        tmp_res.append("(" + x + ")" + y)
            res.append(tmp_res)
        return res[n]