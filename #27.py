# 27.移除元素
# 原地移除所有数值等于val的元素,并返回移除后数组的新长度,不要使用额外数组空间,必须仅适用O(1)额外空间
# 并与原地修改输入数组.元素的顺序可以改变,不需要考虑数组中超出新长度后面的元素
# 解题思路跟刚刚做的#283一样,双指针把目标元素都后移输出左指针的数就是它的长度
# 还有一个优化双指针,避免非目标元素的重复赋值
from typing import List


class Solution:

    def removeElement1(self, nums: List[int], val: int) -> int:
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return j

# 优化双指针时候,循环的地方需要注意,需要考虑到左右指针相同
    def removeElement2(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left


obj = Solution()
num = [0, 1, 2, 2, 3, 0, 4, 2]
val1 = 2
# result = obj.removeElement1(num, val1)
result = obj.removeElement2(num, val1)
print(result)
