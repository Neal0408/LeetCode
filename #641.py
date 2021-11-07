# 641.设计循环双端队列
# 设计实现双端队列.
# 解题思路
# 淦...要提交的时候才发现题目是要求循环(估计这个也是用数组或者链表做的,要求上说不要用内置的双
# 端队列,但是没要求不能用普通队列,可以考虑一下一般队列怎么做.但是一般队列和列表的话都需要反复
# 反转, 想了一下用链表可能会更方便一些.用链表做比较顺没有特别别的问题出现.)
# 思考了一下应该还有挽回的余地.循环数组的话就要注意何时为 Full.


class Node:

    def __init__(self, value: int, nextNode=None):
        self.value = value
        self.next = nextNode


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        newNode = Node(value)
        if self.count >= self.size:
            return False
        else:
            if not self.head:
                self.head = newNode
                self.tail = newNode
                self.head.next = self.tail
                self.tail.next = self.head
                self.count += 1
            else:
                self.tail.next = newNode
                newNode.next = self.head
                self.head = newNode
                self.count += 1
            return True

    def insertLast(self, value: int) -> bool:
        newNode = Node(value)
        if self.count >= self.size:
            return False
        else:
            if not self.tail:
                self.head = newNode
                self.tail = newNode
                self.head.next = self.tail
                self.tail.next = self.head
                self.count += 1
            else:
                self.tail.next = newNode
                self.tail = newNode
                self.tail.next = self.head
                self.count += 1
            return True

    def deleteFront(self) -> bool:
        if not self.head:
            return False
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.count -= 1
            else:
                self.head = self.head.next
                self.count -= 1
            return True

    def deleteLast(self) -> bool:
        if not self.tail:
            return False
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.count -= 1
            else:
                p = self.head
                while p.next != self.tail:
                    p = p.next
                p.next = self.head
                self.tail = p
                self.count -= 1
            return True

    def getFront(self) -> int:
        return -1 if not self.head else self.head.value

    def getRear(self) -> int:
        return -1 if not self.tail else self.tail.value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


obj = MyCircularDeque(3)
