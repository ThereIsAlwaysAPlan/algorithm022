#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-14 16:45:25
# @Author: xiaochuan
# @Description: 367. 有效的完全平方数

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 二分
        left,right = 1,num
        while left <= right:
            mid = left + (right-left)//2
            if mid  > num/mid:
                right = mid -1
            elif mid == num/mid:
                return True
            else:
                left = mid + 1
        return False

        # 牛迭
        # if num < 2:
        #     return True
        # r = num // 2
        # while r*r > num:
        #     r = (r+num//r)//2
        # return r*r == num

if __name__ == "__main__":
    print(Solution().isPerfectSquare(16))