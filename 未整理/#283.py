# 283. 移动零
# 将所有0移动到数组的末尾,同时保持非零元素的相对顺序
# 做这题的时候感觉脑袋有个大病,题目说是保持非零元素相对顺序,我误以为是0元素相对不变...一顿画了半天...服气!
# 正常做的话移动也可以,双指针做,我觉得remove之后再append应该也没啥毛病吧
from typing import List


class Solution:

    def moveZeroes1(self, nums: List[int]) -> None:
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

    def moveZeroes2(self, nums: List[int]) -> None:
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


obj = Solution()
num = [0, 1, 0, 3, 12]
# obj.moveZeroes1(num)
obj.moveZeroes2(num)
# 运行了一下还是双指针比较快,可能是列表自带的remove和append时间比较长
print(num)
