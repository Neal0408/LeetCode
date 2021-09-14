# 217.数组 给定一个整数数组, 判断是否存在重复元素
# 解题思路,Python中有一个set()可以创建一个无序不重复元素集,直接比较nums数组和nums集合的长度就可以得出结果
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


nums1 = [1, 2, 3, 1]
result = containsDuplicate(nums1)
print(result)
