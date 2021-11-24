# 剑指 Offer 30.包含 min 函数的栈
# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、
# push及 pop 的时间复杂度都是 O(1)。
# 解题思路
# 1.用一个栈来记录元素，另一个栈来维护栈内最小元素。弹出时如果 B 栈尾元素和要弹出的元素相同
# 则当前最小值要弹出栈，如果不同则最小值依旧在栈元素中。


class MinStack:

    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        if self.B[-1] == self.A.pop():
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]


obj = MinStack()
