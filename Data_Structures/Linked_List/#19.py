# 19.删除链表的倒数第N个结点
# 给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。
# 解题思路
# 1.一般的方法是遍历两遍。然后找到需要删除节点的前一个节点，然后进行删除操作。
# 2.快慢指针。预留n个位置，快指针如果遇到None则表示已经是链表尾了。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return ListNode()
        dummy = ListNode(-1, head)
        count = 0
        cur = dummy.next
        while cur:
            cur = cur.next
            count += 1
        cur = dummy
        for _ in range(count - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        fast = head
        slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


obj = Solution()
