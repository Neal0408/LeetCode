# 剑指 Offer 09.用两个栈来实现队列
# 用两个栈来实现一个队列。请实现它的两个函数 appendTail 和 deleteHead，分别完成在队列尾部
# 插入整数和在队列头部删除整数的功能。
# 解题思路
# 1.很经典的数据结构题，使用两个栈的目的在于避免列表删除头元素时后面元素都要移动的问题，一个
# 用来正序，一个用来倒序优先弹出倒序部分。之前的逻辑稍微有点繁杂，改一下。两个栈的功能都比较
# 纯粹一点，若B不为空，则直接出队列即可，然后再判断栈A为空则没有元素可以弹出返回-1，有的话依
# 次出栈入栈到B，在出队列。


class CQueue:

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


obj = CQueue()
