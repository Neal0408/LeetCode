# 剑指 Offer 53-2.0 ~ n-1 中缺失的数字
# 一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围 0 ~ n-1 之内。
# 在范围 0 ~ n-1 内的 n 个数字中有且只有一个数字不在该数组中，请找出这个数字。
# 1.最开始有想到二分查找，但是想错时间复杂度了以为跟遍历一样就没往下写。想到求和，想了想跟遍
# 历没啥区别，但是出乎意料的过了样例。所以先用笨方法写一遍然后再用二分法写一遍。
# 2.二分查找的话跟最开始想的差不多，判断m是不是所在位置的值nums[m]。


from typing import List


class Solution:

    # 方法一 求和后做差
    def missingNumber(self, nums: List[int]) -> int:
        # len + 1 是原来该有的长度。
        n = len(nums) + 1
        sum0 = n * (n - 1) / 2
        sum1 = sum(nums)
        return int(sum0 - sum1)

    # 方法二 二分查找
    def missingNumber2(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i


obj = Solution()
