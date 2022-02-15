# 26.删除有序数组中的重复项
# 给你一个升序排列的数组，请你原地删除重复出现的元素，是每个元素只出现一次，返回数组新长度。
# 解题思路
# 1.快慢指针，自己也捣腾出来了只不过非常不熟练还需要琢磨一会儿。
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


obj = Solution()
