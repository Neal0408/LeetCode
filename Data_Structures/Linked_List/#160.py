# 160.相交链表
# 给你两个单链表的头节点，请你找出并返回两个单链表相交的起始节点。
# 解题思路
# 1.第一种方法是使用哈希集合。这种方法比较常规。因为返回的是 ListNode 所以单用列表存储值，认
# 为值相同就是同一个节点的这种想法是错误的。在做的时候看到第一个示例的时候就想到了。所以需要存
# 储节点的信息并且不希望它重复添加，所以用到哈希集合。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        s = set()
        temp = headA
        while temp:
            s.add(temp)
            temp = temp.next
        temp = headB
        while temp:
            if temp in s:
                return temp
            temp = temp.next

        return None


obj = Solution()
