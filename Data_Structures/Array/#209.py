# 209.长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 target。真该从根源该数组满足其和 >=target 的长
# 度最小的连续子数组，并返回其长度。如果不存在复合条件的子数组，返回0。
# 解题思路
# 1.滑动窗口。如果总和小于目标值则持续加 nums[end]，如果总和超过目标值则更新现在的长度，并去
# 掉 nums[start] 元素后后移 start。
from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans


obj = Solution()
