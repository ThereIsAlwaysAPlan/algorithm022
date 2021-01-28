#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-29 00:46:54
# @Author: xiaochuan
# @Description: 37. 解数独
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 保存可填数
        row = [set(range(1,10)) for _ in range(9)]
        col = [set(range(1,10)) for _ in range(9)]
        block = [set(range(1,10)) for _ in range(9)]

        # 初始化，移除已填数，确定空白格
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    block_idx = i//3*3+j//3
                    row[i].remove(num)
                    col[j].remove(num)
                    block[block_idx].remove(num)
                else:
                    empty.append((i,j))
        def dfs(level=0):
            if len(empty) == level:
                return True
            i,j = empty[level]
            block_idx = i//3*3+j//3
            # 回溯试错可填数
            for num in row[i]&col[j]&block[block_idx]:
                row[i].remove(num)
                col[j].remove(num)
                block[block_idx].remove(num)
                board[i][j] = str(num)
                if dfs(level+1):
                    return True
                row[i].add(num)
                col[j].add(num)
                block[block_idx].add(num)
                # board[i][j] = '.' # 该值总会被覆盖，so可不回溯
            return False
        
        dfs(0)
