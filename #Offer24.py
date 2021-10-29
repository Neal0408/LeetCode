# Offer24(206).反转链表
# 给你单链表的头结点 head,请你反转链表,并返回反转后的链表.
# 解题思路
# 1.最开始干想有点没想到,后来看了流程图才一点点推的,迭代做法就是搞个 pre 存前节点, cur 存当
# 前节点,tmp 存后继节点,一步步循环改指向.难道是不难画画图就好了.
# 2.递归就比较巧妙,层层套用循环到 head 为尾时终止并返回,然后重新改指向.这个解释有点不太直观
# ,看一下那个流程图会舒服很多.


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList1(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        cur = self.reverseList2(head.next)
        head.next.next = head
        head.next = None

        return cur


s = Solution()
# 创建链表
var = [1, 2, 3, 4, 5]
dummyRoot = ListNode(0)
ptr = dummyRoot
for i in var:
    ptr.next = ListNode(i)
    ptr = ptr.next
head1 = dummyRoot.next
# 使用方法获取结果
# res = s.reverseList2(head1)
res = s.reverseList1(head1)
