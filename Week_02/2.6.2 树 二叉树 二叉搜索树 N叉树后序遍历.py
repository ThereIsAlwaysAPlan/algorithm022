#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2020-12-26 21:40:06
# @Author: xiaochuan
# @Description: N叉树后序遍历

from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # 递归
        # res = []
        # def dfs(root):
        #     # terminator solution
        #     if not root:
        #         return []
        #     for node in root.children:
        #         dfs(node)
        #     res.append(root.val)
        # dfs(root)
        # return res

        # 迭代 颜色标记法 出栈：左右根  入栈：根右左 
        # 使用stack1 对孩子节点顺序反转后，存入stack中
        # if not root:
        #     return []
        # res = []
        # stack = [(0,root)]
        # while stack:
        #     color,node = stack.pop()
        #     if not node:
        #         continue
        #     if color == 0:
        #         # 先存 根节点
        #         stack.append((1,node))
        #         # 将孩子节点反转顺序后存入stack
        #         # stack1 = []
        #         # for i in node.children:
        #         #     stack1.append((0,i))
        #         # while stack1:
        #         #     stack.append(stack1.pop())
        #         for i in node.children[::-1]:
        #             stack.append((0,i))
        #     else:
        #         res.append(node.val)
        # return res

        # 迭代 栈模拟 后序：左右根  出栈：先根，后压入children，最后结果反转输出即可
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return res[::-1]