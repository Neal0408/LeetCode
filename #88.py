# 88.合并两个有序数组
# 两个非递减顺序数组 num1 和 num2,另有m,n表示元素数目
# 解题思路第一种方法是合并然后排序，但是这种方法没有利用原来数据是有序的条件
# 第二种方法是双指针从前到后比较相对小的元素写在nums1中
# 第三种方法是双指针，从nums1尾部开始比较写入，这种方法就不用额外申请空间因为题目本身为nums1准备了n+m的长度
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
