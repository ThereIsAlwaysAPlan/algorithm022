#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2020-12-23 17:09:36
# @Author: xiaochuan
# @Description: 找雪花

from typing import List


class Solution:
    def findSameSnow(self, snows: List[List[int]]) -> str:
        # hashtable
        # time : O(n*k) n：二维数组长度，k≤72
        # space: O(n*k) n：二维数组长度，k≤12 + tmp1/tmp2 两个列表（every len=6）
        d = {}
        for snow in snows:
            if tuple(snow) in d:
                return 'Yes'
            # 将当前雪花所有相似雪花（正向、逆向）导入dict中
            for i in range(6):
                tmp1 = []  # 正向
                tmp2 = []  # 逆向
                for j in range(6):
                    if i + j >= 6:
                        tmp1.append(snow[i+j-6])
                    else:
                        tmp1.append(snow[i+j])
                for j in range(6):
                    if i - j < 0:
                        tmp2.append(snow[i-j+6])
                    else:
                        tmp2.append(snow[i-j])
                if tuple(tmp1) not in d:
                    d[tuple(tmp1)] = 1
                else:
                    return 'Yes'
                if tuple(tmp2) not in d:
                    d[tuple(tmp2)] = 1
                else:
                    return 'Yes'
        return 'No'


if __name__ == "__main__":
    snows = [[1, 2, 3, 4, 5, 6], [4, 3, 2, 1, 6, 5]]
    print(Solution().findSameSnow(snows))
