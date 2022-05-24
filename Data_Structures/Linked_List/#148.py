# 148.排序链表
# 给你链表的头结点head，请将其按升序排列并返回排序后的链表。
# 解题思路
# 1.这道比较难一些。第一种方法是自顶向下的归并。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 自顶向下的归并排序
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(mid)
        h = res = ListNode(-1)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next


obj = Solution()
