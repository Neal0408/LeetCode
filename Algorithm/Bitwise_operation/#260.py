# 260.只出现一次的数字3
# 给定一个整数数组，其中恰好有两个元素只出现一次，其余所有元素均出现两次。找出只出现一次的那
# 两个元素。你可以按任意顺序返回答案。
# 解题思路
# 1.位运算方法。根据异或的特性出现两次的元素都会被抵消掉。而最后的 x 是由两个不一样的元素异或
# 得来的结果，所以可以把最后的元素分为两类。


from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:
        xorsum = 0
        for num in nums:
            xorsum ^= num

        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num

        return [type1, type2]


obj = Solution()
