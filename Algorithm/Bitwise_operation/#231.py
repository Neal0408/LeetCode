# 231. 2 的幂
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。
# 解题思路
# 1.位运算，2 的幂次方只有最高位为 1 其余为 0，而 n - 1 只有最高位为 0 其余为 1 的特性。


class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


obj = Solution()
