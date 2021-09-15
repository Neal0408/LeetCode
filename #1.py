# 1.两数之和
# 给定一个整数数组nums和一个整数目标值target,请找出能组成目标值的两个整数的下标并返回
# 解题思路,第一反应是最笨的方法,两重循环遍历,第二种方法哈希表,创建哈希,寻找目标元素是否存在于数组中
from typing import List


class Solution:
    # 方法1 循环遍历
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if target == nums[i] + nums[j]:
                    return [i, j]

    # 方法2 哈希表
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                print(hashtable)
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i


nums1 = [2, 7, 11, 1, 3, 12, 15]
target1 = 10
s = Solution()
result1 = s.twoSum1(nums1, target1)
result2 = s.twoSum2(nums1, target1)
print(result1)
print(result2)
