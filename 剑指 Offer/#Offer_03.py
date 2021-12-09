# 剑指 Offer 03.数组中重复的数字
# 找出数组中重复的数字。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重
# 复了几次。请找出数组中任意一个重复的数字。
# 解题思路
# 1.最开始想到的是集合，因为集合只会存储不同元素，然后遍历。
# 2.看的题解，使用的是原地交换。题目中表示长度为 n 数组范围在 0 ~ n-1，所以也就表明索引与值
# 是一对多的关系。所以恢复成顺序就能起到跟字典一样的作用了。
from typing import List


class Solution:

    # 方法一 集合遍历
    def findRepeatNumber(self, nums: List[int]) -> int:
        set1 = set()
        for i in nums:
            if i not in set1:
                set1.add(i)
            else:
                return i
        return -1

    # 方法二 原地交换
    def findRepeatNumber2(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


obj = Solution()
