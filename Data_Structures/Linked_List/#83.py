# 83.删除排序链表中的重复元素
# 给定一个已排序的链表的头head，删除所有重复的元素，使每个元素只出现一次。返回已排序的链表。
# 解题思路
# 1.删除重复元素即可。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


obj = Solution()
