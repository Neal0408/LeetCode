# 剑指 Offer 04.二维数组中的查找
# 在一个 n*m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一个列都按照从上到下递增的
# 顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 解决思路
# 1.有想到对角线元素是左上矩阵的最大值，但是并没能写出来。官方题解的思路就非常清晰，因为每行
# 中最左的元素最小，如果比最左还小那么就不在这行，去掉一行，列也相同原理。开始元素为左下角的
# 元素。
from typing import List


class Solution:

    def finNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


obj = Solution()
