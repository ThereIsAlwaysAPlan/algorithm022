#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-02-07 22:40:30
# @Author: xiaochuan
# @Description: 191. 位1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
        # loop  n & 1 : 判断末位是1还是0，n右移一位
        count = 0
        for _ in range(32):
            if n & 1:
                count += 1
            n >>= 1
        return count
                
        # 位运算 while n > 0 : x = x & (x-1) count ++
        # count = 0
        # while n:
        #     n = n & (n-1)
        #     count += 1
        # return count

        # 掩码 n & mask 判断第n位是否为1
        # count = 0
        # mask = 1
        # for i in range(32):
        #     if n & mask:
        #         count += 1
        #     mask <<= 1
        # return count
