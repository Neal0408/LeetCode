# 剑指 Offer 11.旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。给你一个可能存在重复元素
# 值的数组 numbers，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组
# 的最小元素。
# 解题思路
# 1.自己没做出来，甚至最开始都没太懂题意。看了官方题解，意思就是数组做过旋转找旋转点。题解用
# 的方法是用二分法找到左升序组合右升序组交界的元素就是旋转点。


class Solution:

    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]


obj = Solution()
