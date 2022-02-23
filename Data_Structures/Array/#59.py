# 59.螺旋矩阵2
# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方
# 形矩阵 matrix 。
# 解题思路
# 1.模拟。模拟整个外环向内循环填写的过程。


class Solution:

    def generateMatrix(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1):
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1):
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):
                mat[i][l] = num
                num += 1
            l += 1
        return mat


obj = Solution()
