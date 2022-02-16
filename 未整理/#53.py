# 53.最大子序和
# 给定一个整数数组nums,找到一个具有最大和的连续子数组(子数组最少包含一个元素),返回其最大值
# 动态规划的思路比较好理解,前数之和小于零时去除,大于零时当前是数改写成和
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] = nums[i] + nums[i - 1]
        return max(nums)


s = Solution()
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = s.maxSubArray(nums1)
print(result)
