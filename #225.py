# 225.用队列实现栈
# 请你仅使用两个队列实现一个后入先出(LIFO)的栈,并支持普通栈的全部四种操作.
# 解题思路
# 1.自己做的时候是想着把一个队列作为记录顺序另一个作为一个暂存的队列,在进行栈的 pop 的时候先
# 把栈底即队列首部 get 出来 put 到暂存队列中以记录弹出后的所有栈的元素,并留一个栈顶即队列尾
# 元素进行返回,然后把暂存队列跟顺序队列对换,以确保栈顺序不变.
# 2.官方解法中第一种方法跟我自己想的差不多,第二种方法是用双端队列,记录当前队列元素个数,左弹
# 出右进入已确保队首一直为栈顶元素.这种方法也不难想到,而且代码会比较优雅.


import queue
from collections import deque


class MyStack1:

    def __init__(self):
        self.p1 = queue.Queue()
        self.p2 = queue.Queue()

    def push(self, x: int) -> None:
        self.p1.put(x)

    def pop(self) -> int:
        while self.p1.qsize() > 1:
            self.p2.put(self.p1.get())
        self.p1, self.p2 = self.p2, self.p1
        return self.p2.get()

    def top(self) -> int:
        return self.p1.queue[-1]

    def empty(self) -> bool:
        return self.p1.empty()


class MyStack2:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# s = MyStack1()
s = MyStack2()
