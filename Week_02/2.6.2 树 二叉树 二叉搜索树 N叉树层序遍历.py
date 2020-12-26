#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2020-12-26 23:26:10
# @Author: xiaochuan
# @Description: 层序遍历

from typing import List
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # BFS——deque time:O(n) space:O(n)
        # res = []
        # if not root:
        #     return res
        # queue = collections.deque()
        # queue.append(root)
        # while queue:
        #     level  = []
        #     # 循环当前层的个数（len(queue)）
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level.append(node.val)
        #         queue.extend(node.children)
        #     res.append(level)
        # return res

        # 简化BFS——deque time:O(n) space:O(n)
        # res = []
        # if not root:
        #     return res
        # queue = collections.deque([root])
        # while queue:
        #     res.append([])
        #     # 循环当前层的个数（len(queue)）
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         res[-1].append(node.val)
        #         queue.extend(node.children)
        # return res

        # 简化BFS——双指针 一个指向前置层，一个指向当前层
        # time:O(n) space:O(n)
        # res = []
        # if not root :
        #     return []
        # prev_level = [root]
        # while prev_level:
        #     curr_level = []
        #     res.append([])
        #     for node in prev_level:
        #         res[-1].append(node.val)
        #         curr_level.extend(node.children)
        #     prev_level = curr_level
        # return res

        # 递归  每层递归的时候传入 当前层数
        # time:O(n) space:O(logn),最坏:O(n)  运行在堆栈上的空间
        res = []
        if not root:
            return res

        def traversal(root,level):
            # terminator condition
            if not root:
                return []
            # process current information
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            # extend root.children
            for node in root.children:
                traversal(node,level+1)

        traversal(root,0)
        return res