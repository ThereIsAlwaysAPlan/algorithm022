#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-02 22:56:30
# @Author: xiaochuan
# @Description: 验证二叉搜索树
# 核心思想：利用二叉搜索树的特性：其中序遍历的结果是递增的，然后去判断当前节点的值和其前置节点的值（初始为负无穷大），若 ≤，则返回False
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
class Solution:     
    pre_value = -sys.maxsize
    def isValidBST(self, root: TreeNode) -> bool:
        # 第一种，二叉搜索树特性：其中序遍历结果是递增的
        # if not root:
        #     return True
        
        # if not self.isValidBST(root.left):
        #     return False
        
        # if root.val <= self.pre_value:
        #     return False

        # self.pre_value = root.val

        # return self.isValidBST(root.right)

        # 栈模拟 
        # 核心思想：遍历节点，如果当前节点的值 ≤ 前置节点的值（初始为负无穷大），则返回False，遍历结束，则返回True
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= self.pre_value:
                return False
            self.pre_value = node.val
            root = node.right
        return True
