# 496.下一个更大元素 I
# 给你一个没有重复元素的数组 nums1 和 nums2, 其中 nums1 是 nums2 的子集.请你找出 nums1
# 中每个元素在 nums2 中的下一个比其大的值.
# 解题思路
# 最开始想到的是单调栈,最好还能做哈希对应就可以避免重复计算...但是自己还是没能写出来.
# 看了下官方题解,思路是相同的.循环反转后的 nums2 如果当前栈顶小于 num 则弹出,然后将对应关系
# 存入字典中,再添加当前元素到栈.最后返回 nums1 中元素对应的值.
from typing import List


class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]


s = Solution()
n1 = [4, 1, 2]
n2 = [1, 3, 4, 2]
result = s.nextGreaterElement(n1, n2)
