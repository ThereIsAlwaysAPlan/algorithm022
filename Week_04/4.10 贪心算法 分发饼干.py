#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-14 14:12:27
# @Author: xiaochuan
# @Description: 455. 分发饼干
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 贪心 sort g,s 把刚好合适尺寸的饼干分配给相同胃口（或稍小）的孩子
        # time: O(nlogn + mlogm) space: O(1)
        g.sort()
        s.sort()
        count,p,q = 0,0,0
        while p < len(g) and q < len(s):
            if g[p] <= s[q]:
                count += 1
                p += 1
            q += 1
        return count

if __name__ == "__main__":
    print(Solution().findContentChildren([1,2,3],[1,1]))