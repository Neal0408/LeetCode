# 剑指 Offer 35.复杂链表的复制
# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针
# 指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 Null。
# 解题思路
# 1.自己写还是没能完整写出来。本题的难点在于在复制链表的过程中怎么构建新链表各节点的 random
# 引用指向。在使用哈希表时创建的映射为(原 cur 节点，新 cur 节点)，通过 dic.get(cur.next)
# 来获得对新复制好的节点的引用指向。字典中键值为原节点的对应关系，get 则是获得新创建的节点并
# 进行 new_a1 到 new_b1 引用指向。random 引用指向同理。
class Node:
    
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]


obj = Solution()
