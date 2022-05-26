# 剑指 Offer 30.包含min函数的栈
# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数在该栈中，调用min、push
# 及pop的时间复杂度都是O(1)。
# 解题思路
# 1.用一个栈来记录元素，另一个栈来维护栈内最小元素。弹出时如果 B 栈尾元素和要弹出的元素相同
# 则当前最小值要弹出栈，如果不同则最小值依旧在栈元素中。A or B判断的小细节，即A为真，则B即便
# 报错也是没有关系的。例如代码18行，前面为空，后面即便B[-1]报错也不碍事，前面不为空时后面正
# 常存在。


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
