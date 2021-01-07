from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 在原来的基础上，考虑对重复的部分 剪枝
        # 如何剪枝？
        # 对于选择第i个数，如果这次选择的数跟上一次的一模一样（上一次的已经撤销不选了），
        # 那么也就相当于重复了上一次选择的过程（对于剩余的数组，本次和上次剩余数组是一样的），
        # 这是没有必要的，所以这部分需要略过

        # # 1.为了保证不选到重复数，我们先对数组排序，这样容易去判断
        # nums.sort()
        # # 2.init
        # res,length = [],len(nums)
        # vis = [False]*length
        # # 3.dfs
        # def dfs(level,length,vis,tmp):
        #     # terminator
        #     if level == length:
        #         res.append(tmp.copy())
        #         return
        #     # prepare recursion    
        #     for i in range(length):
        #         # 如果已经访问过，或者数字重复，剪枝
        #         if vis[i] or i > 0 and nums[i] == nums[i-1] and not vis[i-1]:
        #             continue
        #         # process current logic
        #         vis[i] = True
        #         tmp.append(nums[i])
        #         # drill down
        #         dfs(level+1,length,vis,tmp)
        #         # revert current logic
        #         vis[i] = False
        #         tmp.pop()
            
        # dfs(0,length,vis,[])
        # return res

        # 递归，不使用额外空间
        nums.sort()
        res,length = [],len(nums)

        # 对数组左右边界进行全排列  有点问题
        def dfs(left,right):
            # terminator
            if left == right-1:
                print('end: left = {},nums = {}'.format(left,nums))
                res.append(nums.copy())
                return
            # drill down
            for i in range(left,right):
                # 去重
                if i != left and nums[i] == nums[left]:
                    continue
                nums[i],nums[left] = nums[left],nums[i]
                print('prev: i = {} left = {},nums = {}'.format(i,left,nums))
                dfs(left+1,right)
                nums[i],nums[left] = nums[left],nums[i]
                print('after: i = {} left = {},nums = {}'.format(i,left,nums))

        dfs(0,length)
        return res
    
if __name__ == "__main__":
    print(Solution().permuteUnique([1,2,2,1]))