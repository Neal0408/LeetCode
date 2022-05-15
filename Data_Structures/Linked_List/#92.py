# 92.反转链表2
# 请你反转从位置left到位置right的链表节点，返回反转后的链表。
# 解题思路
# 1.在206的基础上做改动。分别找到左右操作节点，切段节点后反转区间节点后重新连接。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse(head: ListNode):
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        dummy = ListNode(-1, head)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        l_node = pre.next
        r_node = pre
        for _ in range(right - left + 1):
            r_node = r_node.next
        curr = r_node.next

        pre.next = None
        r_node.next = None

        reverse(l_node)
        pre.next = r_node
        l_node.next = curr
        return dummy.next

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy.next


obj = Solution()
