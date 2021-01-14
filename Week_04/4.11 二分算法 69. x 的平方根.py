class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分 单调 存在上下界，index
        # left,right = 0,x
        # while left <= right:
        #     mid  = left + (right-left)//2
        #     # 考虑中位数平方溢出
        #     if mid*mid > x:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return right

        # 牛顿迭代法
        r = x
        while r*r>x:
            r = (r+x/r)/2
        return int(r)            


if __name__ == "__main__":
    print(Solution().mySqrt(16))