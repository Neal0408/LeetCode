# 27.移除元素
# 给你一个数组和一个值，你需要原地移除所有数值等于val的元素，并返回移除后数组的新长度。
# 解题思路
# 1.典型双指针问题，左右指针逐步把不等于val的移到前面。还有一种双指针优化的方法就是一前一后
# 的左右逼近的方法。这种方法即便right等于目标值，第二遍循环的时候就会被right - 1替代掉。所
# 以没有关系的。
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left


obj = Solution()
