from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 思路一，使用队列存储节点信息，每次遍历长度为当前队列长度，遍历时将子节点信息推入队内
# 思路二，使用双指针，当前指针记录父节点信息，遍历当前指针指向的节点列表，记录节点值到结果集，并用next指针记录子节点信息
# 思路三，递归，使用level保存当前层数，将本层节点的值记录到本层结果集
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # bfs——deque
        # if not root:
        #     return []
        # res = []
        # q = collections.deque()
        # q.append(root)
        # while q:
        #     res.append([])
        #     for i in range(len(q)):
        #         tmp = q.popleft()
        #         res[-1].append(tmp.val)
        #         if tmp.left:
        #             q.append(tmp.left)
        #         if tmp.right:
        #             q.append(tmp.right)
        # return res

        # bfs——双指针
        # if not root:
        #     return []
        # curr = [root]
        # res = []
        # while curr:
        #     res.append([])
        #     nxt = []
        #     for node in curr:
        #         res[-1].append(node.val)
        #         if node.left:
        #             nxt.append(node.left)
        #         if node.right:
        #             nxt.append(node.right)
        #     curr = nxt
        # return res

        # 递归
        res = []
        def dfs(level,root):
            # terminator
            if not root:
                return []
            # process current logic
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            # drill down
            dfs(level+1,root.left)
            dfs(level+1,root.right)
        dfs(0,root)
        return res