class Solution:
    def climbStairs(self, n: int) -> int:
        # fn = fn-1 + fn-2  最优重复性
        # 不需要保存中间变量，O(n)
        # 动态规划
        f1,f2,f3 = 1,2,3
        if n < 3 : return n
        else:
            for _ in range(3,n+1):
                f3 = f2 + f1
                f1 = f2
                f2 = f3
        return f3

        # recursion Fibnacci O(2^n)
        # def fib(n):
        #     if n <= 2:
        #         return n
        #     else:
        #         return fib(n-1) + fib(n-2)

        # return fib(n)

if __name__ == "__main__":
    print(Solution().climbStairs(10))