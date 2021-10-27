# Offer59-1(239).滑动窗口的最大值
# 给定一个数组nums和滑动窗口的大小k，请找出所有滑动窗口里的最大值.
# 解题思路
# 1.切片窗口大小,取最大值写入需要返回的列表中,在题目中没看到对时间复杂度的要求,但翻了下题解
# 说是时间复杂度超了.!! 过了几天又重新翻看了一下这个,因为当时第一个方法直接通过的就没多想,是
# 因为在剑指Offer页面做的,翻了题库中的 239 题提交相同代码才显示超时,原因是因为前者的测试用
# 例很简单不会超时.
# 2.优先队列,使用堆队列的大根堆特性维护最大值,以及将即将离开滑动窗口的元素删除.
# 3.单调队列,需要同时弹出队尾和队首元素所以需要使用双端队列.
import collections
from typing import List
import heapq


class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        result = []
        if len(nums) > 0:
            for i in range(len(nums) - k + 1):
                result.append(max(nums[i: i + k]))
        return result

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            # 小于滑动窗口左侧的数据弹出
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans

    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        # 第一个窗口部分
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans


s = Solution()
num1 = [1, 3, -1, -3, 5, 3, 6, 7]
# res = s.maxSlidingWindow1(num1, 3)
# res = s.maxSlidingWindow2(num1, 3)
res = s.maxSlidingWindow3(num1, 3)
