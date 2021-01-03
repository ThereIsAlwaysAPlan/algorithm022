#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-03 18:21:08
# @Author: xiaochuan
# @Description: 最近公共祖先
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1.暴力 找到p的所有祖先，其中一个必定是q的祖先，去找 后序遍历（栈模拟）
# 递归分治思想：如果p，q分别在左右子树，那么最近公共祖先是根节点；如果p，q都在左子树，那么最近公共祖先也在左子树上，p，q都在右子树上；则最近公共祖先也在右子树上
# 后序遍历的思想：只有知道了左右子树的结果（p,q是否在异侧），才能返回根节点的结果


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # terminator
        # if not root:
        #     return None
        # # process current level
        # if root.val == p.val or root.val == q.val: return root
        # # drill down (split subproblems)
        # l = self.lowestCommonAncestor(root.left,p,q)
        # r = self.lowestCommonAncestor(root.right,p,q)
        # # merge subresults
        # if l and r : return root
        # if not r : return l
        # if not l : return r

        if root in (None, p, q):
            return root
        left, right = (self.lowestCommonAncestor(node, p, q)
                       for node in (root.left, root.right))
        return root if left and right else left or right
