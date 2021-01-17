# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
from typing import List
class Solution:
    minest = -sys.maxsize
    def largestValues(self, root: TreeNode) -> List[int]:
        # 思路：bfs deque 双指针 dfs:递归
        # 双指针
        if not root:
            return []
        curr = [root]
        res = []
        while curr:
            res.append(self.minest)
            nxt = []
            for node in curr:
                res[-1] = max(res[-1],node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            curr = nxt
        return res