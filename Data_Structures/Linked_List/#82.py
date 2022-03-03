# 82.删除排序链表中的重复元素2
# 给定一个已排序的链表的头，删除原始链表中所有重复数字的节点，只留下不同的数字。
# 解题思路
# 1.单次遍历。因为头节点可能需要被删除，所以使用一个虚拟节点辅助操作。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


obj = Solution()
