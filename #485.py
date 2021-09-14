# 485.数组 给定一个二进制数组,计算其中最大连续1的个数
# 问题比较常规,解题思路是遇到1计数,数量记录在maxCount里面取最大值
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    maxCount = count = 0

    for i, num in enumerate(nums):
        if num == 1:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 0
    maxCount = max(maxCount, count)
    return maxCount


nums1 = [1, 1, 0, 1, 1, 1]
Count = findMaxConsecutiveOnes(nums1)
print(Count)
