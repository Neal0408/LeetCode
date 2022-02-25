# 137.只出现一次的数字2
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并
# 返回那个只出现了一次的元素。
# 解题思路
# 1.逻辑电路设计，对两个整数看做整体写出真值表并设计逻辑电路。
from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b


obj = Solution()
