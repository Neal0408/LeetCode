# 剑指 Offer 24.反转链表
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
# 解题思路
# 1.自己写的时候还是没能顺利写出来。节点替换以及最开始设置的节点总是会卡壳。循环还是要一个节
# 点一个节点做最基础操作，循环才不容易出错。
# 2.递归也比较容易理解。递归后继节点，到最后cur为空时为终止条件，在回溯时修改节点引用指向。


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur:
                return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res

        return recur(head, None)


obj = Solution()
