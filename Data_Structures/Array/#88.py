# 88.合并两个有序数组
# 给你两个按非递减顺序排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n，分别表示 nums1
# 和 nums2 中的元素数目。请你合并两个数组并使合并后的数组同样按非递减顺序排列。
# 解题思路
# 1.合并之后排序，这是一种偷懒的方式只是单单能通过问题，并没有考虑到题目想考察的点。
# 2.双指针从前到后比较后写入临时列表中。最后将 nums1 用临时列表替换。
# 3.第三种方法比较自然，因为 nums1 中已经开辟好了空间，从后向前写就不需要临时列表了。
from typing import List


class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        s1 = []
        p1 = p2 = 0
        while p1 < m or p2 < n:
            if p1 == m:
                s1.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                s1.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                s1.append(nums1[p1])
                p1 += 1
            else:
                s1.append(nums2[p2])
                p2 += 1

        nums1[:] = s1

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[p] = nums1[m - 1]
                p = p - 1
                m = m - 1
            else:
                nums1[p] = nums2[n - 1]
                p = p - 1
                n = n - 1
        if n > 0:
            nums1[:n] = nums2[:n]


n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]
s = Solution()
# s.merge1(n1, 3, n2, 3)
# s.merge2(n1, 3, n2, 3)
s.merge3(n1, 3, n2, 3)
