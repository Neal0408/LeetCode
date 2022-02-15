# 15.三数之和
# 判断 nums 中是否存在三个元素之和为 0？，请找出所有和为0且不重复的三元组。
# 解题思路
# 1.最容易想到的就是暴力遍历，循环所有可能的三元组符合要求的记录下来。果然还是超时，测试用例
# 在 315/318 的时候卡住了，所以其实元素少的话暴力也不是不行。这个样例有三千个数据所以很显然
# 会超时。需要找另一种方法。
# 2.第二个想到的是找对称的元素，排序是很有必要的操作。但是具体实现还是有点想不出来，看了题解
# 果然题解就是题解很值得学习。左右逼近的思想。
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] ==0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1
        return res


obj = Solution()
