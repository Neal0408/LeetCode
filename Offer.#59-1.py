# 59-1(239).滑动窗口的最大值
# 给定一个数组nums和滑动窗口的大小k，请找出所有滑动窗口里的最大值
# 解题思路
# 1.切片窗口大小，取最大值写入需要返回的列表中
# 2.
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if len(nums) > 0:
            for i in range(len(nums) - k + 1):
                result.append(max(nums[i: i + k]))
        return result


s = Solution()
num1 = [1, 3, -1, -3, 5, 3, 6, 7]
result1 = s.maxSlidingWindow(num1, 3)
