#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-29 23:59:51
# @Author: xiaochuan
# @Description: 433. 最小基因变化

from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 双向bfs
        # 预处理
        if end not in bank:
            return -1
        front = {start}
        back = {end}
        bank = set(bank)
        dist = 0
        
        while front:
            dist += 1
            nxt = set()
            for gene in front:
                for i in range(8):
                    for c in ('A','C','G','T'):
                        if gene[i] != c:
                            new_gene = gene[:i] + c + gene[i+1:]
                            if new_gene in back:
                                return dist
                            if new_gene in bank:
                                nxt.add(new_gene)
                                bank.remove(new_gene)
            front = nxt
            if len(front)>len(back):
                front,back = back,front
        return -1