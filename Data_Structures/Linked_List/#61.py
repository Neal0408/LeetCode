# 61.旋转链表
# 给你一个链表的头节点 head，旋转链表，将链表每个节点向右移动 k 个位置。
# 解题思路
# 1.大致思路是对的，但是最近赶论文时间不够没能写对。k mod n 的想法也想到了。剩下就是解题技巧
# 形成环形链表然后寻找断点。
# 2.第二次做这个题已经能写的很顺畅了。链表的题画图还是yyds，流程搞清楚了就没问题了。
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

    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(next=head)
        pre = dummy
        n = 0
        while pre.next:
            n += 1
            pre = pre.next
        pre.next = dummy.next
        for _ in range(n - k % n):
            pre = pre.next
        dummy.next = pre.next
        pre.next = None
        return dummy.next


obj = Solution()
