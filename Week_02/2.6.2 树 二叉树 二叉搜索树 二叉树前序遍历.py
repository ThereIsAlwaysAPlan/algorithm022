from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归 O(n)
        # if not root:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # 颜色标记法 0:未访问 1：已访问
        # res = []
        # stack = [(0,root)]
        # while stack:
        #     color,node = stack.pop()
        #     if not node:
        #         continue
        #     if color == 0:
        #         stack.append((0,node.right))
        #         stack.append((0,node.left))
        #         stack.append((1,node))
        #     else:
        #         res.append(node.val)
        # return res

        # 栈模拟 先弹出根节点，然后右子树，左子树依次入栈
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

        # morris time:O(n) space:O(1)