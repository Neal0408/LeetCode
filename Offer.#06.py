# Offer.06 输入一个链表的头节点,从尾到头反过来返回每个节点的值(用数组返回)
# 典型递归,先走到链表末端,回溯时依次将节点值val加入列表后返回
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head == None:
            return []
        return self.reversePrint(head.next) + [head.val]


nums = [1, 3, 2]
dummyRoot = ListNode(0)
ptr = dummyRoot
for num in nums:
    ptr.next = ListNode(num)
    ptr = ptr.next
ptr = dummyRoot.next
s = Solution()
result = s.reversePrint(ptr)
print(result)
