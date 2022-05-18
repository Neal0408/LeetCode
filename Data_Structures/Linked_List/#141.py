# 141.环形链表
# 给你一个链表的头节点head，判断链表中是否有环。
# 解题思路
# 1.自己做的类似于官方的方法一，但是官方用的是集合来存储已经遍历过的节点我用的是列表。同样能
# 够解决问题但是列表会慢许多。还是采取集合的方式比较好。
# 2.快慢指针，原本以为时间上循环会很多，但是意想不到速度很快。类似龟兔赛跑，乌龟一次一步，兔
# 子一次两步如果有环兔子必定在某节点与乌龟相遇。


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


obj = Solution()
