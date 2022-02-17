# 16.最接近的三数之和
# 给你一个长度为n的整数数组nums和一个目标值target。请你从中选出三个整数，使它们的和与target
# 最接近。返回这三个数的和。
# 解题思路
# 1.三重循环求和后与目标值做差找到最小值。但是早该想到的本题主要考察就是减小时间复杂度，从而
# 避免超时。所以一开始作为陷阱的三重循环必然不通过，实际也写了很显然没通过。后面就需要排序加
# 双指针，利用有序这个属性来减小时间复杂度。
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                Sum = nums[i] + nums[start] + nums[end]
                if abs(target - Sum) < abs(target - ans):
                    ans = Sum
                if Sum == target:
                    return Sum
                elif Sum > target:
                    end -= 1
                elif Sum < target:
                    start += 1
                else:
                    return ans
        return ans


obj = Solution()
