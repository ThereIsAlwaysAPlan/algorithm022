#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2020-12-26 22:20:42
# @Author: xiaochuan
# @Description: N叉树前序遍历   

from typing import List
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 递归
        # res = []   
        # def dfs(root):
        #     # terminator
        #     if not root:
        #         return []
        #     # process curr level
        #     res.append(root.val)
        #     # extend nodes
        #     for node in root.children:
        #         dfs(node)
        # dfs(root)
        # return res

        # 迭代 栈模拟 
        # res = []
        # stack = [root]
        # if not root:
        #     return res
        # while stack:
        #     # 根节点出栈
        #     node = stack.pop()
        #     res.append(node.val)
        #     # 子节点 从右到左依次 压入栈中
        #     for i in node.children[::-1]:
        #         stack.append(i)
        # return res

        # 迭代 颜色标记法  前序：根——左——右  入栈：右——左——根
        if not root:
            return []
        res = []
        stack = [(0,root)]
        while stack:
            color,node = stack.pop()
            if not node:
                continue
            if color == 0:
                for i in node.children[::-1]:
                    stack.append((0,i))
                stack.append((1,node))
            else:
                res.append(node.val)
        return res