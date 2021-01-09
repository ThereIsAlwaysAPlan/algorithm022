from typing import List

# 思路：loop grid,meet land first so land_num + 1 then transfer land to water and dfs up down left right
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #     row_length = len(grid)
        #     col_length = len(grid[0])

        #     def dfs(i, j):
        #         # terminator
        #         if i < 0 or j < 0 or j > col_length-1 or i > row_length-1 or grid[i][j] != '1':
        #             return
        #         grid[i][j] = '0'
        #         dfs(i-1, j)
        #         dfs(i+1, j)
        #         dfs(i, j-1)
        #         dfs(i, j+1)
        #     count = 0
        #     for i in range(row_length):
        #         for j in range(col_length):
        #             if grid[i][j] == '1':
        #                 count += 1
        #                 dfs(i, j)
        #     return count

        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                # sink(i-1,j)
                # sink(i+1,j)
                # sink(i,j-1)
                # sink(i,j+1)
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))) # 比较转化为list才会执行内部函数，这样的话开销比较大
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


if __name__ == "__main__":
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(Solution().numIslands(grid))
