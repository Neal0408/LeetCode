# 10-2.青蛙跳台阶问题
# 一只青蛙以此可以跳上 1 级台阶,也可以跳上 2 级台阶.求该青蛙跳上 n 级台阶总共有多少种跳法.
# 解题思路
# 画一画图会比较清楚,n(3) = n(2) + n(1),以此类推.与菲波那切数列不同的是 n(1) 为 1, n(2)
# 为 2.


class Solution:

    def numWays(self, n: int) -> int:
        a, b = 1, 2
        while n > 1:
            a, b = b, (a + b) % 1000000007
            n -= 1
        return a


obj = Solution()
