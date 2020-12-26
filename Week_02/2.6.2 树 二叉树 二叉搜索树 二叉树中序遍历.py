from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归 常规
        # res = []
        # def dfs(root):
        #     if not root:
        #         return None
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return res

        # 递归 romantic写法 前序、后序写法类似，仅顺序调换
        # terminator
        # if not root:
        #     return [] 
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # 迭代 栈模拟 time:O(n) space:O(h+n+1) h:树的高度
        # stack = []
        # res = []
        # while stack or root:
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         tmp = stack.pop()
        #         res.append(tmp.val)
        #         root = tmp.right
        # return res

        # 颜色标记法  模拟栈 
        # 前序：出栈：根——左——右  入栈：右——左——根
        # 中序：出栈：左——根——右  入栈：右——根——左
        # 后续：出栈：左——右——根  入栈：根——左——右
        # 优化：如果子节点为空，不需要入栈
        WHITE,GRAY = 0,1
        res = []
        stack = [(WHITE,root)]
        while stack:
            color,node = stack.pop()
            if not node: continue
            if color == WHITE:
                if node.right:
                    stack.append((WHITE,node.right))
                stack.append((GRAY,node))
                if node.left:
                    stack.append((WHITE,node.left))
            else:
                res.append(node.val)
        return res