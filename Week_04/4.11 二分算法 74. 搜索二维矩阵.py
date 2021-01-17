import bisect
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从右上开始搜索 确定行，之后用二分
        # 边界判断
        # if target < matrix[0][0] or target > matrix[-1][-1]:
        #     return False
        # # 找到行
        # row = 0
        # while row < len(matrix) and target > matrix[row][len(matrix[row])-1]:
        #     row += 1
        # # 二分
        # left,right = 0,len(matrix[row])-1
        # while left <= right:
        #     mid = left + (right-left)//2
        #     if matrix[row][mid] == target:
        #         return True
        #     elif matrix[row][mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return False


        # 整体二分
        # if target < matrix[0][0] or target > matrix[-1][-1]:
        #     return False
        # n = len(matrix[0])
        # left,right = 0,len(matrix)*n-1
        # while left <= right:
        #     mid = left + (right-left)//2
        # 注意点：除数和取余的数都是n，而不是m
        # 测试用例 [1,1] 2 || [1,3] 2
        #     num = matrix[mid//n][mid%n] 
        #     if num == target:
        #         return True
        #     elif num > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return False


        # 使用bisect模块
        # bisect.bisect 对于一个有序数组，返回target将在数组中的位置，但是不会做插入
        i = bisect.bisect(matrix, [target])
        # 本行第一个数就是target，返回
        if i < len(matrix) and matrix[i][0] == target:
            return True
        # 如果不是本行，就去一行找答案
        row = matrix[i-1]
        j = bisect.bisect_left(row, target)
        return j < len(row) and row[j] == target


        # return bool(matrix) and target in matrix[bisect.bisect(matrix, [target + 0.5]) - 1]  