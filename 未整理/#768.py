# 768.最多能完成排序的块II
# 这道题是压根没搞懂。。。 到时候先做769再做这个好了。。
from typing import List


class Solution:

    def maxChunksTOSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                head = stack.pop()
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(head)
            else:
                stack.append(num)
        return len(stack)


obj = Solution()
