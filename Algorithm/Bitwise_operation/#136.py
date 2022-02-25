# 136. 只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了
# 一次的元素。
# 解题思路
# 1.这道题是从训练营的位运算专题接触到的，所以一开始就用的异或去做的题。
from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res


obj = Solution()
