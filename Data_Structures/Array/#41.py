# 41.缺失的第一个正数
# 给你一个未排序的整数数组 nums，请你找出其中没有出现的最小的正整数。请你实现时间复杂为 O(n)
# 并且只使用常数级别额外空间的解决方法。
# 解题思路
# 1.最开始不太懂题目想要考察的内容在哪里只会单纯的暴力循环。官方题解中的哈希表的办法也看了好
# 久才理解。其意图在于在固定长度中的数组中记录更多信息。首先要清楚的是对于一个 N 长度的数组，
# 其没有出现的最小正整数只能在 [1,N+1] 中。当遍历到数 x 且在范围[1,N]中时候，对应位置 x-1
# 的元素取负号来对应记录当前 x 已被标记，如果[1,N]中的元素都被标记了那么答案是 N+1，如果没
# 有被标记则对应元素下标+1 则为那个缺失的最小的正整数值。
# 2.置换的方法稍微好理解一些，将数组恢复到原来序列其中第一个不符合顺序的数的下标+1则为缺失值。
from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
    
    def firstMissingPositive2(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


obj = Solution()
