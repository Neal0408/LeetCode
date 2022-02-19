# 155.最小栈
# 设计一个支持 push，pop，top操作，并能在常熟时间内检索到最小元素的栈。
# 解题思路
# 1.比较经典的设计题，用一个辅助栈来保存现在的最小值。但是写的还是没有题解简约。还是值得学习。
import math


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(min(val, self.stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]


obj = MinStack()
