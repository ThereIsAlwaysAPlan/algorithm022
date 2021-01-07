from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 递归，第一层有n种选择，第二层n-1种选择，第n层一种选择，用一个set存储本次选择已保存的数字
        # 排列递归：全排列 n!  每次拷贝结果数组：n  ∴time:O(n*n!)  space:O(n)  choose n + 系统栈 n
        # length = len(nums)
        # res = []
        # tmp = []
        # choose = [False]*length
        # def dfs(level,length,choose,tmp):
        #     # terminator
        #     if level == length:
        #         res.append(tmp.copy())
        #         return
        #     # se
        #     for i in range(length):
        #         if not choose[i]:
        #             choose[i] = True
        #             tmp.append(nums[i])
        #             dfs(level+1,length,choose,tmp)
        #             choose[i] = False
        #             tmp.pop()
        # dfs(0,length,choose,tmp)
        # return res

        # 递归 + 剪枝，不使用额外空间，将已选择的放左边，未选择的放右边，space:O(n) -> O(1)
        # length = len(nums)
        # res = []
        # def recursion(curr):
        #     # terminator
        #     if curr == length:
        #         res.append(nums[:]) # 浅拷贝

        #     # drill down
        #     for i in range(curr,length):
        #         # 交换 curr 和 i，让已选择的在左边
        #         nums[i],nums[curr] = nums[curr],nums[i]
        #         recursion(curr+1)
        #         # 撤销交换操作
        #         nums[i],nums[curr] = nums[curr],nums[i]
            
        # recursion(0)
        # return res

        # 调用库函数解决
        # return list(map(list, itertools.permutations(nums)))
        # return list(itertools.permutations(nums))

        # 将任何一个数作为第一个数，然后递归剩余数组
        # return nums and [[n] + p for i,n in enumerate(nums) for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

        # 把当前数组中的第一个数，在剩余数组的任意位置递归
        # return nums and [p[:i] + [nums[0]] + p[i:] for p in self.permute(nums[1:]) for i in range(len(nums))] or [[]]

        # 使用reduce，将数组中的下一个数，插入到已经建好的排列中
        from functools import reduce
        return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                    for p in P for i in range(len(p)+1)],
                    nums, [[]])

if __name__ == "__main__":
    print(Solution().permute([1,2,3]))