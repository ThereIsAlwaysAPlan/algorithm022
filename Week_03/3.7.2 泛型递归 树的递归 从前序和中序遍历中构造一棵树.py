#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-03 21:44:16
# @Author: xiaochuan
# @Description: 
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 通过前序遍历找其root，通过中序遍历确定其左右子树
        # 前序：【根，【左子树】，【右子树】】
        # 中序：【【左子树】，根，【右子树】】
        # 通过前序确定根，再找到根在中序中的位置，即可确定左右子树的长度
        # 而同一棵树，左右子树的长度是一致的，其遍历的长度自然也是一致的
        # 通过hashtable映射快速获取中序遍历中值与索引的对应关系
        get_in_root_idx = {value:idx for idx,value in enumerate(inorder)}
        print(get_in_root_idx)
        def recursion(pre_left,pre_right,in_left,in_right):
            # terminator
            if pre_left > pre_right:
                return None
            # 根节点即前序第一个节点
            pre_root_idx = pre_left
            # 获取中序遍历中根节点的索引
            print(pre_root_idx,preorder[pre_root_idx])
            in_root_idx = get_in_root_idx[preorder[pre_root_idx]]
            # 获取左子树的长度
            left_length = in_root_idx - in_left
            # 建立当前层的根节点
            root = TreeNode(preorder[pre_root_idx])
            # 遍历左子树
            root.left = recursion(pre_left+1,pre_left+left_length,in_left,in_root_idx-1)
            # 遍历右子树
            root.right = recursion(pre_left+left_length+1,pre_right,in_root_idx+1,in_right)
            # return
            return root
        n = len(preorder)
        return recursion(0,n-1,0,n-1)

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(Solution().buildTree(preorder,inorder))