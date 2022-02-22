# 704.二分查找
# 给定一个n个元素有序的整型数组nums和一个目标值target，写一个函数搜索nums中的target，如果
# 目标值存在返回下标否则返回-1。
# 解题思路
# 1.典型的二分查找。主要难点在于临界条件的判断，不能乱写容易遗漏元素。
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


obj = Solution()
