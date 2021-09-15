# Offer.30 包含min函数的栈
# 定义栈的数据结构,实现一个能够得到栈的最小元素的min函数,时间复杂度为O(1)
# 解题思路为,因为需要时间复杂度为O(1),所以说明可能需要一个变量去存储最小值以及为维护需要时直接输出


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
