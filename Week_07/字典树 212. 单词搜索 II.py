#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-26 22:55:21
# @Author: xiaochuan
# @Description: 212. 单词搜索 II
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 思想：字典树Trie + 剪枝（已遍历过的单词将其从字典树上抹去，防止有检索相似单词时重复遍历，比如 pa，paa这种）
        # time:O(l_words + m*n*l_word) space:O(w)   
        # l_words:words中所有字符串相加的长度 l_word:words其中某一个字符串的长度  w：words的长度
        m,n = len(board),len(board[0])
        if not board or not board[0] or not words:
            return []
        
        # 实现Trie insert_word
        root = {}
        end_of_words = '#'

        def insert_word(words):
            for word in words:
                node = root
                for char in word:
                    node = node.setdefault(char,{})
                node[end_of_words] = word # 终止符保存当前单词
        
        # 实现dfs
        res = set()
        # 四联通
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        def search_dfs(i,j,curr_dict):
            # terminator
            c = board[i][j]
            # 判断是否到了最后
            end = curr_dict[c].pop(end_of_words,False)
            if end:
                res.add(end)

            # process current logic
            tmp,board[i][j] = board[i][j],'@'  # 将走过的路径标识为@
            for k in range(4):
                _i,_j = i+dx[k],j+dy[k]
                # drill down
                if 0<=_i<m and 0<=_j<n and board[_i][_j] in curr_dict[c]:
                    search_dfs(_i,_j,curr_dict[c])
            # revert currnt logic
            board[i][j] = tmp
            # 消除已遍历的单词，防止重复遍历
            if not curr_dict[c]:
                curr_dict.pop(c)
                
        # 遍历
        insert_word(words)
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    search_dfs(i,j,root)
        return list(res)
# 借用字典树的核心思想（但并未创建字典树），直接遍历所有单词，dfs时按照单词字母顺序遍历
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         n, m = len(board), len(board[0])

#         shot = defaultdict(list)
#         for i in range(n):
#             for j in range(m):
#                 shot[board[i][j]].append((i, j))

#         road = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#         def go(w, index, x, y):
#             if index == len(w):
#                 return True
#             r[x][y] = 0
#             for a, b in road:
#                 i, j = x + a, y + b
#                 if -1 < i < n and -1 < j < m and r[i][j] and board[i][j] == w[index] and go(w, index + 1, i, j):
#                     return True
#             r[x][y] = 1
#             return False
        
#         res = []
#         for w in words:
#             for x, y in shot[w[0]]:
#                 r = [[1] * m for _ in range(n)]
#                 if go(w, 1, x, y):
#                     res.append(w)
#                     break
#         return res