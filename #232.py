# 232.用栈实现队列
# 请你仅使用两个栈实现先入先出队列.队列应当支持一般队列支持的所有操作.
# 解题思路
# 1.Python 这边是没有单独 stack 的数据结构的,所以使用 list 来实现,题目中要求只能使用标准
# 栈的操作.我的想法比较常规,倒序存储到 s2 后弹出即弹出队首元素,然后再倒序到 s1.
# 2.看了下题解,大致没啥问题,我的解答有一处有点冗余,倒序弹出之后不用急着再倒序回来,输出的时候
# 可以先判断 s2 不为空的话就先弹出.


class MyQueue1:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        ans = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return ans

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return not self.s1


class MyQueue2:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# s = MyQueue1()
s = MyQueue2()
