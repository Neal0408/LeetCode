# 剑指 Offer 06.从尾到头打印链表
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值(用数组返回)。
# 解题思路
# 1.用递归是比较好理解的，如果当前节点不为空调用 next 节点 + 当前节点值，然后一直调用到当前
# 节点为空时返回空列表。
from typing import List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        else:
            return self.reversePrint(head.next) + [head.val]


obj = Solution()
