# 78.子集
# 给你一个整数数组 nums，数组中的元素互不相同。返回该数组所有可能的子集（幂集）。
# 解题思路
# 1.使用位运算来记录所有子集，0 则代表不在子数组中，1 则代表在子数组中。
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        # 子集合的总个数。
        n = 1 << size
        res = []
        for i in range(n):
            cur = []
            for j in range(size):
                # 结果为 1 则为选中进子集合中。可以列真值表查看其结果和排列组合是一样的。
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res


obj = Solution()
