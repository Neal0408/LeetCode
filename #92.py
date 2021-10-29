# 92.反转链表 II
# 给你单链表的头指针 head 和两个整数 left 和 right,其中 left <= right.请你反转从位置 le
# ft 到位置 right 的链表节点,返回反转后的链表.
# 解题思路
# 1.是那个 206 题的后续,官方的第一个方法比较单纯就是结合 206 题,先找到左前和右后的节点,切段
# 链接然后中间需要反转的链表使用前面题的步骤做完,再重新链接左前和右后节点.只不过有点冗余.
# 2.第二种方法的思路就比较清晰,每个需要反转的节点从左节点头插入,也可以保证是一次遍历.


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween1(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_linked_list(head: ListNode):
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp

        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        for _ in range(left - 1):
            pre = pre.next

        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next

        left_node = pre.next
        curr = right_node.next

        pre.next = None
        right_node.next = None

        reverse_linked_list(left_node)

        pre.next = right_node
        left_node.next = curr
        return dummy_node.next

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next


s = Solution()
