#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-27 23:33:49
# @Author: xiaochuan
# @Description: 547. 省份数量
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m,n = len(isConnected),len(isConnected[0])

        # dfs time:O(n) space:O(n)
        vis = [False]*n
        def dfs(vis,i):
            for j in range(n):
                if not vis[j] and isConnected[i][j] == 1:
                    vis[j] = True
                    dfs(vis,j)
        count = 0
        for i in range(m):
            if not vis[i]:
                # 每次dfs都能连一个省份（最起码能连它自己） ∴count+1没毛病
                dfs(vis,i)
                count+=1
        return count

        # 并查集 time:O(n^2) space:O(n)
        # p = [i for i in range(n)]
        # count = n

        # def find(p,i):
        #     root = i
        #     while p[root] != root:
        #         root = p[root]
        #     # 路径压缩
        #     while p[i] != i:
        #         x=i
        #         i = p[i]
        #         p[x] = root
        #     return i
        
        # def union(p,i,j):
        #     nonlocal count
        #     p1 = find(p,i)
        #     p2 = find(p,j)
        #     if p1 == p2:
        #         return True
        #     p[p1] = p2
        #     count -= 1
        #     return False
        
        # for i in range(m):
        #     for j in range(i,n):
        #         if isConnected[i][j]:
        #             union(p,i,j)
        # return count

        # 第三方包 
        # 1.报错 异常
        # import scipy.sparse
        # return scipy.sparse.csgraph.connected_components(M)[0]

        # 2.报错 异常
        # import numpy as np
        # return len(set(map(tuple, (np.matrix(M, dtype='bool')**len(M)).A)))