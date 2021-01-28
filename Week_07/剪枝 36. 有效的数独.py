#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-29 00:45:53
# @Author: xiaochuan
# @Description: 
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 对每个单元格都单独进行行列的合法性判断 O(1) :729次
        # def isValid(row,col,char):
        #     for i in range(9):
        #         if i != col and board[row][i] != '.' and board[row][i] == char:
        #             return False
        #         if i != row and board[i][col] != '.' and board[i][col] == char:
        #             return False
        #         if row//3*3+i//3 == row and col//3*3+i%3 == col:
        #             continue
        #         block = board[row//3*3+i//3][col//3*3+i%3]
        #         if block != '.' and block == char:
        #             return False
        #     return True
        
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] != '.':
        #             if not isValid(i,j,board[i][j]):
        #                 return False
        # return True

        # 计算每行每列每块数字出现的次数，超过1，则不合法  
        # time:O(1) : 81次
        row  = [{} for _ in range(9)]
        col  = [{} for _ in range(9)]
        block  = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                block_idx = i//3*3+j//3
                if num != '.':
                    row[i][num] = row[i].get(num,0)+1
                    col[j][num] = col[j].get(num,0)+1
                    block[block_idx][num] = block[block_idx].get(num,0)+1
                    # print(row[i],col[j],block[block_idx])
                    if row[i][num] > 1 or col[j][num] > 1 or block[block_idx][num] > 1:
                        return False
        return True