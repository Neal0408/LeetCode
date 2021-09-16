# 203.移除链表元素
# 给head和val,删除满足Node.val == val的节点,并返回新的头节点
# 解题思路,遍历迭代的主要思想是p.next.val == val时 p.next = p.next.next
# 即当下个节点的值跟目标值相同时指针指向跳过下一个节点,指向下下一个节点
# 递归的话先递归到尾节点,然后判断当前val是否等于val,如果等于跳过当前节点,如果不等于则保留当前节点


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 迭代
    def removeElement1(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p:
            # 这里的p.next and是判断p.next非空时进行后面判断
            if p.next and p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next

    # 递归
    def removeElement2(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        head.next = self.removeElement2(head.next, val)
        if head.val == val:
            next_node = head.next
        else:
            next_node = head
        return next_node


A = [1, 2, 6, 3, 4, 5, 6]
val1 = 6
p = q = ListNode()
for i in A:
    p.next = ListNode(i)
    p = p.next
q = q.next
obj = Solution()
# result = obj.removeElement1(q, val1)
result = obj.removeElement2(q, val1)
