from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心 假设能全局最优，看能否实现初始最优
        # 能到达的最后位置
        # can_arrive = len(nums)-1
        # for i in range(len(nums)-1,-1,-1):
        #     # 判断第i步是否可以到达最后位置
        #     if nums[i] + i >= can_arrive:
        #         can_arrive = i
        # return can_arrive == 0

        # 使用变量记录当前能到达的最大位置，初始为0
        # 如果当前位置超过最大位置，那么遍历结束：返回False
        # 遍历结束，或者能到达最后点，返回True
        m = 0
        length = len(nums)
        for i in range(length):
            if i > m:
                return False
            m = max(m,i+nums[i])
            if m >= length:
                return True
        return True

        # one line 写法有问题
        # return functools.reduce(lambda m, (i, n): max(m, i+n) * (i <= m), enumerate(nums, 1),1) > 0

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))