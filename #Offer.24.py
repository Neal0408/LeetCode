# Offer.24(#206) 反转链表
# 定义一个函数,输入一个链表的头结点,反转该链表并输出反转后链表的头节点
# 解题思路,自己写的时候还是很笨重,先在数组中存储数值,再反转再重头开始重新创建新的链表,但代码不够优雅
# 在别人的题解中迭代是只使用的一个循环来完成的,还有利用Python平行语言赋值语法特性进一步简化
# 另外一种思路就是递归,很巧妙但是想一次写对比较有难度


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    
    def reverseList2(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def reverseList3(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res

        return recur(head, None)


p = q = ListNode(0)
for i in range(1, 6):
    p.next = ListNode(i)
    p = p.next
q = q.next
obj = Solution()
# result = obj.reverseList1(q)
# result = obj.reverseList2(q)
result = obj.reverseList3(q)
