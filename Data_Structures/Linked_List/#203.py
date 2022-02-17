# 203.移除链表元素
# 给你一个链表的头节点head和一个整数val，请你删除链表中与val值相同的节点，并返回新的头节点。
# 解题思路
# 1.这一次还是比较顺畅的写完了，稍微有点进步。然后整理了链表中的指针和对象关系的笔记。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        pre = dummy
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next


obj = Solution()
