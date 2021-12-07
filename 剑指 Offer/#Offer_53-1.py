# 剑指 Offer 53-1.在排序数组中查找数字
# 统计一个数字在排序数组中出现的次数。
# 解题思路
# 1.虽然最开始是想到的二分查找，但是没把握一次写对，就拿最笨方法遍历来做之后再去想二分查找。
# 2.排序数组中所有数字 target 形成一个窗口，记窗口左右边界为 left 和 right，分别对应窗口左
# 右的首个元素。题目要求的 target 出现次数则是右边界 - 左边界 - 1。


from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        count = 0
        if target not in nums:
            return 0
        else:
            for i in nums:
                if i < target:
                    continue
                elif i == target:
                    count += 1
                elif i > target:
                    break
        return count

    def search2(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i
        if j >= 0 and nums[j] != target:
            return 0
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j
        return right - left - 1


obj = Solution()
obj.search2([5, 7, 8, 8, 8, 9], 8)
