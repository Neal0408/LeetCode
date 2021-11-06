# Offer10-1.菲波那切数列
# 写一个函数,输入 n,求斐波那契数列的第 n 项.
# 解题思路
# 动态规划从前往后算,用菲波那切数列公式作为转移方程,从计算效率和空间复杂度上来看都是最好的.


class Solution:

    def fib(self, n: int):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a


obj = Solution()
