# 1.暴力 O(N^2)
# 2.DP
# 子问题 只要连续，那么每个数都乘，if nums[i] < 0,max -> min ma = max(ma,1)*nums[i] mi = min(mi,1)*nums[i]
# 首先由于负数的原因，那么会出现这种负负得正最后求得最大子序列乘积的存在，最小的，乘以一个负数，就变成了最大的，我们因此引入fmin值，并在当前值为负数时，将fmax与fmin的值对换
# 原始一维数组,fmax = max(nums[i],fmax*nums[i],fmin*nums[i]),fmin = min(nums[i],fmax*nums[i],fmin*nums[i]) res = max(res,fmax)
# DP array ma,mi
# DP equation
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # DP
        res = ma = mi = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                ma, mi = mi, ma
            ma = max(ma*nums[i], nums[i])
            mi = min(mi*nums[i], nums[i])
            res = max(res, ma)
        return res

        # others
        # 就是一个奇数个负数或者偶数个负数累乘的问题,要考虑有为0的情况
        # 那么就可以扫两次，一次从左往右计算乘积值，并记录途中的最大值，一次从右往左，也是同理
        # 之所以需要扫两次，是对于累乘的特性，若是从左往右，一直到0之前的数，如果是奇数个负数，从左往右累乘可能得不到最大值，那么从右往左可以补上这部分的最大乘积，
        # 比如:[1,-1,3,5,0,6]，累乘最大值应为15，但是从左往右只能得到最大6，加上从右往左扫一遍就能得到15
        # time:O(n) space:O(n) 实现
        opposite, length = nums[::-1], len(nums)
        for i in range(1, length):
            nums[i] *= nums[i-1] or 1
            opposite[i] *= opposite[i-1] or 1
        return max(nums+opposite)
        # time:O(n) space:O(1) 实现
        ma, length = nums[0], len(nums)
        for x in (1, -1):
            value = 1
            for i in range(length)[::x]:
                value *= nums[i]
                ma = max(value, ma)
                if nums[i] == 0:
                    value = 1
        return ma
