# 622.设计循环队列
# 设计你的循环队列实现.
# 解题思路
# 要求是不要使用内置队列库,得想想用什么存队列.可能需要指针头指针和尾指针.做的时候发现还需要记
# 录一个元素个数.做的时候发现如果用头指针和尾指针的话不太好判断何时为空何时为满,所以还是需要一
# 个记录元素个数的变量,元素个数等于容器长度就表示已经满了.看了题解还有一种用链表做的,用链表的
# 好处是不会为未使用的容量预分配内存.但是官方题解中的链表有点问题并不是循环链表,需要在enQueue
# 中重新把尾指针的 next 指向 head.


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.count = 0
        self.size = k
        self.p = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            return False
        self.queue[(self.p + self.count) % self.size] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.p = (self.p + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.p]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.p + self.count - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


class Node:

    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyCircularQueue2:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            return False

        if self.count == 0:
            self.head = self.tail = Node(value)
            self.head.next = self.tail
            self.tail.next = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# obj = MyCircularQueue(6)
obj = MyCircularQueue2(3)
