# 414.第三大的数
# 给你一个非空数组，返回此数组第三大的数。如果不存在，则返回数组中最大的数。
# 解题思路
# 1.给定的数组进行排序后，遍历数组，如果数组相邻元素相同则找下一个不同的元素直至找到第三不同
# 元素并返回，如果没有找到就返回最大元素。
from typing import List
from sortedcontainers import SortedList


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        diff = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                diff += 1
                if diff == 3:
                    return nums[i]
        return nums[0]

    def thirdMax2(self, nums: List[int]) -> int:
        s = SortedList()
        for num in nums:
            if num not in s:
                s.add(num)
                if len(s) > 3:
                    s.pop(0)
        return s[0] if len(s) == 3 else s[-1]


obj = Solution()
