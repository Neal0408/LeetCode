# 54.螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 解题思路
# 1.模拟。
from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        m = len(matrix)
        n = len(matrix[0])
        l, r, t, b = 0, n - 1, 0, m - 1
        ans = []
        while l <= r and t <= b:
            for i in range(l, r + 1):
                ans.append(matrix[t][i])
            for i in range(t + 1, b + 1):
                ans.append(matrix[i][r])
            if l < r and t < b:
                for i in range(r - 1, l, -1):
                    ans.append(matrix[b][i])
                for i in range(b, t, -1):
                    ans.append(matrix[i][l])
            l, r, t, b = l + 1, r - 1, t + 1, b - 1
        return ans


obj = Solution()
obj.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
