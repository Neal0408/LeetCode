# 977.有序数组的平方
# 给你一个按非递减顺序排序的整数数组 nums，返回每个数字的平方组成的新数组，要求也按非递减顺
# 序排序。
# 解题思路
# 1.双指针比较然后把大的写下来，这是比较常规思想的做法。
from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] ** 2 > nums[j] ** 2:
                ans[pos] = nums[i] ** 2
                i += 1
            else:
                ans[pos] = nums[j] ** 2
                j -= 1
            pos -= 1

        return ans


obj = Solution()
