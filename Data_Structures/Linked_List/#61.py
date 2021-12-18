# 61.旋转链表
# 给你一个链表的头节点 head，旋转链表，将链表每个节点向右移动 k 个位置。
# 解题思路
# 1.大致思路是对的，但是最近赶论文时间不够没能写对。k mod n 的想法也想到了。剩下就是解题技巧
# 形成环形链表然后寻找断点。
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        if (add := n - k % n) == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret


obj = Solution()
