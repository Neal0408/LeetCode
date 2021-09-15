# Offer.09 两个栈实现队列
# 队列特性为先进先出,而栈为先进后出,为了实现队列特性需要实现appendTail和deleteHead
# 为了实现这两个功能,需要一个栈为队列正序一个为队列倒序以便于删除队列头部元素


class CQueue:

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


c = CQueue()
