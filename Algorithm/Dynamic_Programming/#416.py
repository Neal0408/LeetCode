# 416.分割等和子集
# 给你一个只包含正整数的非空数组 nums。请你判断是否可以讲这个数组分割成两个子集,使得两个子集
# 的元素和相等。
# 解题思路
# 1.最开始想到的是所有元素和的一半为目标值，然后求出和为目标值的组合。最开始做的时候是按目标
# 值减去第一个元素后是否存在于列表中，提交发现只通过了 96 测试用例，没有考虑到减去后的目标值
# 是由剩余多个数组元素的组合构成的。最后做出来的也有点奇怪，更像暴力解法。
# 2.后来了解到这个是个0-1背包问题。转移方程，二维数组的最后一项则为最终的答案。问题比较经典
# 可以多看一看。
from typing import List


class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2

        def inside(target, nums, cache):
            if target in nums:
                return True
            if target == 0:
                return True
            if target < 0:
                return False
            if target in cache:
                return False
            cache.add(target)
            for i, n in enumerate(nums):
                if inside(target - n, nums[i + 1:], cache):
                    return True
            return False

        return inside(target, nums, set())

    def canPartition2(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if n < 2:
            return False
        if total % 2 != 0:
            return False
        target = total // 2
        if target < max(nums):
            return False

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]

    def canPartition3(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]


obj = Solution()
a = [1, 5, 7, 9]
res = obj.canPartition3(a)
